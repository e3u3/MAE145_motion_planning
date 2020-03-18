#A53307224
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import intervals as I
import matplotlib.pyplot as plt

def samplemethod(mu=0, sigma=0.5, x_t = 0, u_t = 0):
    if u_t == 0:
        x_t_1 = x_t
    elif x_t in I.closed(-50, -49) and u_t == -1:
        x_t_1 = x_t
    elif x_t in I.closed(49, 50) and u_t == 1:
        x_t_1 = x_t
    else:
        tmp1 = scipy.stats.norm(0,sigma).cdf(-1)
        tmp2 = scipy.stats.norm(0,sigma).cdf(1)
        n = tmp2 - tmp1 #the cumulation over [-1,1]
        n = 1/n #normalizer
        y_max = n/np.sqrt(2*np.pi * sigma) * np.exp(-(0)**2/(2*sigma))
        u = np.random.uniform(0, y_max)
        v = np.random.uniform(-1, 1)
        proba = n/np.sqrt(2*np.pi * sigma) * np.exp(-(v)**2/(2*sigma))
        while u > proba:
            u = np.random.uniform(0, y_max)
            v = np.random.uniform(-1, 1)
            proba = n/np.sqrt(2*np.pi * sigma) * np.exp(-(v)**2/(2*sigma))
        x_t_1 = x_t + u_t + v
    return x_t_1
def sensor_method(x_t_1 = 0, z_t = 0):
    if x_t_1 in I.closed(0.5, 1) or x_t_1 in I.closed(2, 2.5) or x_t_1 in I.closed(22.5, 23):
        if z_t == 1:
            return 0.7
        elif z_t == 0:
            return 0.3
        else:
            print("Invalid input z_t")
            return 0
    else:
        if z_t == 1:
            return 0.15
        elif z_t == 0:
            return 0.85
        else:
            print("Invalid input z_t")
            return 0
def draw_particles(index, particles):
    plt.title("This is " + str(index) + "th time")
    for i in particles:
        plt.vlines(i, 0, 1, colors = "b", linestyles = "dashed")
    plt.savefig(str(index)+".png")
    plt.pause(0.1)
def rejection_sampling(x_t, proba):
    c = np.random.uniform(0, 1)
    if c >= proba:
        return True
    else:
        return False
def particle_fileter(u_t, z_t, number = 5):
    plt.ion()
    #initialization
    particles = np.random.uniform(-50, 50, number)
    proba = [1 / number] * number
    plt.cla()
    draw_particles(-1, particles)
    #prediction & update
    for i in range(0, len(u_t)):
        particles_tmp = [0] * number
        for j in range(0, len(particles)):
            particles_tmp[j] = samplemethod(mu = 0, sigma = 0.5, x_t = particles[j], u_t = u_t[i])
            proba[j] = proba[j] * sensor_method(particles_tmp[j], z_t[i])
        sum_cr = sum(proba)
        for j in range(0, len(particles)):
            proba[j] = proba[j] / sum_cr #normalization
        for j in range(0, len(particles)):
            index = int(np.floor(np.random.uniform(0, len(particles))))
            repeat = rejection_sampling(particles_tmp[index], proba[index])
            while repeat:
                index = int(np.floor(np.random.uniform(0, len(particles))))
                repeat = rejection_sampling(particles_tmp[index], proba[index])
            particles[j] = particles_tmp[index]
            proba[j] = 1 / number
        plt.cla()
        draw_particles(i, particles)
    plt.ioff()
    plt.show()
if __name__ == "__main__":
    u_t = [1]*14+[0]*2+[-1]*22
    z_t = [0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0]
    number = 10
    particle_fileter(u_t, z_t, number)
