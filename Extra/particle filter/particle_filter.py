import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from read_data import read_world, read_sensor_data
from python_program_p2 import predict
#add random seed for generating comparable pseudo random numbers
np.random.seed(123)

#plot preferences, interactive plotting mode
plt.axis([-1, 12, 0, 10])
plt.ion()
plt.show()

def plot_state(particles, landmarks, map_limits):
    # Visualizes the state of the particle filter.
    #
    # Displays the particle cloud, mean position and landmarks.
    
    xs = []
    ys = []

    for particle in particles:
        xs.append(particle['x'])
        ys.append(particle['y'])

    # landmark positions
    lx=[]
    ly=[]

    for i in range (len(landmarks)):
        lx.append(landmarks[i+1][0])
        ly.append(landmarks[i+1][1])

    # mean pose as current estimate
    estimated_pose = mean_pose(particles)

    # plot filter state
    plt.clf()
    plt.plot(xs, ys, 'r.')
    plt.plot(lx, ly, 'bo',markersize=10)
    plt.quiver(estimated_pose[0], estimated_pose[1], np.cos(estimated_pose[2]), np.sin(estimated_pose[2]), angles='xy',scale_units='xy')
    plt.axis(map_limits)

    plt.pause(0.01)
def initialize_particles(num_particles, map_limits):
    # randomly initialize the particles inside the map limits

    particles = []

    for i in range(num_particles):
        particle = dict()

        # draw x,y and theta coordinate from uniform distribution
        # inside map limits
        particle['x'] = np.random.uniform(map_limits[0], map_limits[1])
        particle['y'] = np.random.uniform(map_limits[2], map_limits[3])
        particle['theta'] = np.random.uniform(-np.pi, np.pi)

        particles.append(particle)

    return particles

def mean_pose(particles):
    # calculate the mean pose of a particle set.
    #
    # for x and y, the mean position is the mean of the particle coordinates
    #
    # for theta, we cannot simply average the angles because of the wraparound 
    # (jump from -pi to pi). Therefore, we generate unit vectors from the 
    # angles and calculate the angle of their average 

    # save x and y coordinates of particles
    xs = []
    ys = []

    # save unit vectors corresponding to particle orientations 
    vxs_theta = []
    vys_theta = []

    for particle in particles:
        xs.append(particle['x'])
        ys.append(particle['y'])

        #make unit vector from particle orientation
        vxs_theta.append(np.cos(particle['theta']))
        vys_theta.append(np.sin(particle['theta']))

    #calculate average coordinates
    mean_x = np.mean(xs)
    mean_y = np.mean(ys)
    mean_theta = np.arctan2(np.mean(vys_theta), np.mean(vxs_theta))

    return [mean_x, mean_y, mean_theta]

def sample_motion_model(odometry, particles):
    # Samples new particle positions, based on old positions, the odometry
    # measurements and the motion noise 
    # (probabilistic motion models slide 27)
    # odometry data
    delta_rot1 = odometry['r1']
    delta_trans = odometry['t']
    delta_rot2 = odometry['r2']

    # the motion noise parameters: [alpha1, alpha2, alpha3, alpha4]
    noise = [0.1, 0.1, 0.05, 0.05]

    # generate new particle set after motion update
    new_particles = []
    for particle in particles:
        tmp = [particle['x'],particle['y'],particle['theta']]
        u_t = [delta_rot1,delta_rot2,delta_trans]
        tmp_1 = predict(tmp,u_t,noise)
        particle = dict()
        particle['x'] = tmp_1[0][0]
        particle['y'] = tmp_1[1][0]
        particle['theta'] = tmp_1[2][0]
        new_particles.append(particle)

    return new_particles

def eval_sensor_model(sensor_data, particles, landmarks):
    # Computes the observation likelihood of all particles, given the
    # particle and landmark positions and sensor measurements
    # (probabilistic sensor models slide 33)
    #
    # The employed sensor model is range only.

    sigma_r = 0.2
    #measured landmark ids and ranges

    weights = []

    ids = sensor_data['id']
    ranges = sensor_data['range']
    print(ids)
    print(landmarks)
    for particle in particles:
        tmp_x = particle['x']
        tmp_y = particle['y']
        tmp_t = particle['theta']
        p = 1
        for i in range(0, len(ids)):
            m_x = landmarks[ids[i]][0]
            m_y = landmarks[ids[i]][1]
            tmp_r = np.sqrt((m_x-tmp_x)**2+(m_y-tmp_y)**2)
            p *= 1/np.sqrt(2*np.pi * 0.2**2) * np.exp(-(ranges[i] - tmp_r)**2 / (2 * 0.2**2))
        weights.append(p)
    #normalize weights
    normalizer = sum(weights)
    weights = weights / normalizer
    return weights

def resample_particles(particles, weights):
    # Returns a new set of particles obtained by performing
    # stochastic universal sampling, according to the particle weights.

    particle_list = np.arange(0, 1000)
    new_particles = np.random.choice(particles, 1000, p = weights)


    return new_particles

def main():
    # implementation of a particle filter for robot pose estimation

    print("Reading landmark positions")
    landmarks = read_world("./data/world.dat")
    #read the landmarks one time
    print("Reading sensor data")
    sensor_readings = read_sensor_data("./data/sensor_data.dat")
    # read the sensor_data one time
    #initialize the particles
    map_limits = [-1, 12, 0, 10]
    particles = initialize_particles(1000, map_limits)
    #run particle filter
    for timestep in range(int(len(sensor_readings)/2)): #update times

        #plot the current state
        plot_state(particles, landmarks, map_limits)
        #predict particles by sampling from motion model with odometry info
        #first time
        new_particles = sample_motion_model(sensor_readings[timestep,'odometry'], particles)

        #calculate importance weights according to sensor model
        weights = eval_sensor_model(sensor_readings[timestep, 'sensor'], new_particles, landmarks)

        #resample new particle set according to their importance weights
        particles = resample_particles(new_particles, weights)

    plt.show('hold')

if __name__ == "__main__":
    main()