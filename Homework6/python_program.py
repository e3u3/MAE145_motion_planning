#A53307224
import numpy as np
import matplotlib.pyplot as plt

def samplenormaldistribution(mu=0, sigma=1, size=1):
    sigma = np.sqrt(sigma)
    u = np.random.uniform(size=size)
    v = np.random.uniform(size=size)
    z = np.sqrt(-2*np.log(u))*np.cos(2*np.pi*v)
    z = mu+z*sigma
    proba = 1/(np.sqrt(2*np.pi) * sigma) * np.exp(-(z - mu)**2 / (2 * sigma**2))
    return z,proba

if __name__ == "__main__":
    #for section (i)
    mu = 100
    sigma_2 = 15
    X = []
    Y = []
    for i in range(0,10000):
        x,y = samplenormaldistribution(mu, sigma_2)
        X.append(x[0])
        Y.append(y[0])
    plt.plot(X,Y,'*')
    plt.show()
    #for section (ii)
    control_input = [1] * 10
    X = [0] * 11
    for i in range(0,10):
        x,y = samplenormaldistribution(0,1)
        x = x[0]
        print(x)
        X[1+i] = X[i]+control_input[i]+x
    print(X)
