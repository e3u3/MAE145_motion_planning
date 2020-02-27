#A53307224
import math as mt
import matplotlib.pyplot as plt
import numpy as np
def show_results(X,Y,title):
    plt.scatter(X,Y,color='r',marker='o')
    plt.title(title)
    plt.xlim((0,1))
    plt.ylim((0,1))
    plt.show()
def is_number(val):
    if type(val) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False
def prime_test(p):
    if p > 1:
        for i in range(2,p):
            if (p%i) == 0:
                return False
        else:
            return True
    else:
        return False
def computeGridSukharev(n):
    n=mt.sqrt(n)
    if not is_number(n):
        raise ValueError("The number of the samples along axis should be an integer!")
    _X=[]
    _Y=[]
    C=np.linspace(0+1/(2*n),1-1/(2*n),n)
    for i in C:
       _X.append(np.linspace(0+1/(2*n),1-1/(2*n),n))
       _Y.append(np.linspace(i,i,n))
    X=_X
    Y=_Y
    return X,Y
def computeGridRandom(n):
    if not is_number(n):
        raise ValueError("The number of the samples should be an integer!")
    _X=np.random.sample(n)
    _Y=np.random.sample(n)
    X=_X
    Y=_Y
    return X,Y
def computeGridHalton(n,p1,p2):
    if not is_number(n):
        raise ValueError("The number of the samples should be an integer!")
    if not prime_test(p1):
        raise ValueError("p1 must be a prime number!")
    if not prime_test(p2):
        raise ValueError("p2 must be a prime number!")
    _X=np.linspace(0,0,n)
    _Y=np.linspace(0,0,n)
    for i in range(0,n):
        p1_tmp = i+1
        f1 = 1/p1
        p2_tmp = i+1
        f2 = 1/p2
        while p1_tmp > 0:
            q=p1_tmp//p1
            r=p1_tmp%p1
            _X[i]=_X[i]+f1*r
            p1_tmp=q
            f1=f1/p1
        while p2_tmp > 0:
            q=p2_tmp//p2
            r=p2_tmp%p2
            _Y[i]=_Y[i]+f2*r
            p2_tmp=q
            f2=f2/p2
    X=_X
    Y=_Y
    return X,Y
if __name__ == '__main__':
    title=["Sukharev Grid","Random Grid","Halton Grid"]
    number_samples = 10**2
    if number_samples < 0:
        raise ValueError("The number of samples must be larger than zero")
    X,Y = computeGridSukharev(number_samples)
    show_results(X,Y,title[0])
    X,Y = computeGridRandom(number_samples)
    show_results(X,Y,title[1])
    X,Y = computeGridHalton(number_samples,2,3)
    show_results(X,Y,title[2]) 
    
