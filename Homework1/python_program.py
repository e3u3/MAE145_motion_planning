#A53307224
import math as mt
import numpy as np
import intervals as I
def computeLineThroughTwoPoints(p1,p2):
    x1=p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    if y1-y2!=0:
        a=1/(mt.sqrt(1+np.square((x1-x2)/(y1-y2))))
        b=-((x1-x2)/(y1-y2))*a
        c=-x1*a-y1*b
        return a,b,c
    elif x1==x2:
        return 0,0,0
    else:
        return 0,1,-y1
def computeDistancePointToLine(q,p1,p2):
    a,b,c=computeLineThroughTwoPoints(p1,p2)
    x=q[0]
    y=q[1]
    D=abs(a*x+b*y+c)/1
    return D
def computeDistancePointToSegment(q,p1,p2):
    a,b,c=computeLineThroughTwoPoints(p1,p2)
    if a==0: #horizontal line
        x_inter=q[0]
        y_inter=p1[1]
        D_to_line=abs(y_inter-q[1])
        D_to_p1=mt.sqrt(np.square(q[0]-p1[0])+np.square(q[1]-p1[1]))
        D_to_p2=mt.sqrt(np.square(q[0]-p2[0])+np.square(q[1]-p2[1]))
        p_min=min(p1[0],p2[0])
        p_max=max(p1[0],p2[0])
        if x_inter in I.open(p_min,p_max):
            return D_to_line,0
        else:
            if D_to_p1<D_to_p2:
                return D_to_line,1
            else:
                return D_to_line,2
    if b==0:#vertical line
        x_inter=p1[0]
        y_inter=q[1]
        D_to_line=abs(x_inter-q[0])
        D_to_p1=mt.sqrt(np.square(q[0]-p1[0])+np.square(q[1]-p1[1]))
        D_to_p2=mt.sqrt(np.square(q[0]-p2[0])+np.square(q[1]-p2[1]))
        p_min=min(p1[1],p2[1])
        p_max=max(p1[1],p2[1])
        if y_inter in I.open(p_min,p_max):
            return D_to_line,0
        else:
            if D_to_p1<D_to_p2:
                return D_to_line,1
            else:
                return D_to_line,2
    #The last situation,a common line
    slope1=-a/b
    intersect1=-c/b
    slope2=b/a
    intersect2=q[1]-slope2*q[0]
    x_inter=(intersect2-intersect1)/(slope1-slope2)
    y_inter=x_inter*slope2+intersect2
    D_to_line=mt.sqrt(np.square(x_inter-q[0])+np.square(y_inter-q[1]))
    D_to_p1=mt.sqrt(np.square(q[0]-p1[0])+np.square(q[1]-p1[1]))
    D_to_p2=mt.sqrt(np.square(q[0]-p2[0])+np.square(q[1]-p2[1]))
    p_min=min(p1[0],p2[0])
    p_max=max(p1[0],p2[0])
    if x_inter in I.open(p_min,p_max):
        return D_to_line,0
    else:
        if D_to_p1<D_to_p2:
            return D_to_line,1
        else:
            return D_to_line,2
if __name__=='__main__':
    p1=[1,1]
    p2=[2,2]
    q=[3,4]
    q1=[1,2]
    q2=[10,8]
    q3=[-10,8]
    a,b,c=computeLineThroughTwoPoints(p1,p2)
    if (a,b,c)==(0,0,0):
        print("p1 and p2 must be two different points!")
    else:
        D,w=computeDistancePointToSegment(q1,p1,p2)
        print(D,w)
        D,w=computeDistancePointToSegment(q2,p1,p2)
        print(D,w)
        D,w=computeDistancePointToSegment(q3,p1,p2)
        print(D,w)
