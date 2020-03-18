#A53307224
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import intervals as I
import matplotlib.pyplot as plt

def motion_model(length, ut):
    A = np.zeros([length, length])
    for i in range(length):
        next_p = i + ut
        if next_p >= length:
            next_p = length - 1
        elif next_p <= 0:
            next_p = 0
        A[next_p, i] += 0.5
        next_p = i + 2 * ut
        if next_p >= length:
            next_p = length - 1
        elif next_p <= 0:
            next_p = 0
        A[next_p, i] += 0.25
        A[i,i] += 0.25
    return A
def draw_particles(index, particles):
    plt.title("This is " + str(index) + "th time")
    X = np.arange(len(particles))+1
    plt.bar(X, particles, alpha=0.9, width = 0.35, facecolor = 'lightskyblue', edgecolor = 'white', label='one', lw=1)
    plt.axis([0, 21, 0, 1])
    plt.savefig(str(index)+".png")
    plt.pause(0.4)
    
if __name__ == "__main__":
    plt.ion()
    u = [1]*9 + [-1]*3
    bel = np.hstack ((np.zeros(10), 1, np.zeros(9)))
    draw_particles(-1, bel)
    for i in range(0, len(u)):
        bel = motion_model(len(bel), u[i]) @ bel.T
        bel = bel.T
        sum_cr = sum(bel)
        plt.cla()
        draw_particles(i, bel)
        print(sum(bel))
    plt.ioff()
    plt.show()
