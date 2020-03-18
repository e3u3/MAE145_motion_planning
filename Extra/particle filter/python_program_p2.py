#A53307224
import numpy as np
import matplotlib.pyplot as plt

def samplenormaldistribution(mu=0, sigma=1, size=1):
    sigma = np.sqrt(sigma)
    u = np.random.uniform(size=size)
    v = np.random.uniform(size=size)
    z = np.sqrt(-2*np.log(u))*np.cos(2*np.pi*v)
    z = mu+z*sigma
    return z

def predict(x_t, u_t, alpha):
    b1 = alpha[0]*np.square(u_t[0])+alpha[1]*np.square(u_t[1])
    b2 = alpha[2]*np.square(u_t[2])+alpha[3]*(np.square(u_t[1])+np.square(u_t[0]))
    u_t[0] = u_t[0] - samplenormaldistribution(0, b1)
    u_t[1] = u_t[1] - samplenormaldistribution(0, b1)
    u_t[2] = u_t[2] - samplenormaldistribution(0, b2)
    x_t_plus_1 = x_t
    x_t_plus_1[0] += u_t[2]*np.cos(x_t[2] + u_t[0])
    x_t_plus_1[1] += u_t[2]*np.sin(x_t[2] + u_t[0])
    x_t_plus_1[2] += (u_t[0] + u_t[1])
    return x_t_plus_1

if __name__ == "__main__":
    X_t_plus_1 = []
    Y_t_plus_1 = []
    for i in range(0, 5000):
        x_t = [2,4,0]
        u_t = [np.pi/2, 0, 1]
        alpha = [0.1, 0.1, 0.01, 0.01]
        x_t_plus_1 = predict(x_t,u_t,alpha)
        x_t_plus_1[0] = x_t_plus_1[0][0]
        x_t_plus_1[1] = x_t_plus_1[1][0]
        x_t_plus_1[2] = x_t_plus_1[2][0]
        X_t_plus_1.append(x_t_plus_1[0])
        Y_t_plus_1.append(x_t_plus_1[1])
    plt.plot(X_t_plus_1,Y_t_plus_1,'*')
    plt.show()
        
    
