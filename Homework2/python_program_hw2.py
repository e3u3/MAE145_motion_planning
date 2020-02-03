#A53307224
import math as mt
import matplotlib.pyplot as plt
import numpy as np
import intervals as I
def computeLineThroughTwoPoints(p1,p2): #from homework1
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
def computeDistancePointToSegment(q,p1,p2): #from homework1 with a little adjustment
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
            return (D_to_line,0)
        else:
            if D_to_p1<D_to_p2:
                return (D_to_p1,1)
            else:
                return (D_to_p2,2)
    if b==0:#vertical line
        x_inter=p1[0]
        y_inter=q[1]
        D_to_line=abs(x_inter-q[0])
        D_to_p1=mt.sqrt(np.square(q[0]-p1[0])+np.square(q[1]-p1[1]))
        D_to_p2=mt.sqrt(np.square(q[0]-p2[0])+np.square(q[1]-p2[1]))
        p_min=min(p1[1],p2[1])
        p_max=max(p1[1],p2[1])
        if y_inter in I.open(p_min,p_max):
            return (D_to_line,0)
        else:
            if D_to_p1<D_to_p2:
                return (D_to_p1,1)
            else:
                return (D_to_p2,2)
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
        return (D_to_line,0)
    else:
        if D_to_p1<D_to_p2:
            return (D_to_p1,1)
        else:
            return (D_to_p2,2)
def computeDistancePointToPolygon(q,mypolygon):
    D=[]
    IN=[]
    vertices_number=len(mypolygon)
    for index in range(0,vertices_number):
        if(index!=vertices_number-1):
            tmp=computeDistancePointToSegment(q,mypolygon[index],mypolygon[index+1])
            d=tmp[0]
            i=tmp[1]
            D.append(d)
            IN.append(i)
        else:
            tmp=computeDistancePointToSegment(q,mypolygon[index],mypolygon[0])
            d=tmp[0]
            i=tmp[1]
            D.append(d)
            IN.append(i)
    D_min=min(D)
    print("The distance from q to the polygon is:",D_min)
    index=D.index(D_min)
    if(index!=vertices_number-1):
        return (mypolygon[index],mypolygon[index+1],IN[index])
    else:
        return (mypolygon[index],mypolygon[0],IN[index])
def computeTangentVectorToPolygon(q,tmp):
    u_vector=[]
    if(tmp[2]==0):
        u_vector=(tmp[0][0]-tmp[1][0],tmp[0][1]-tmp[1][1])
    if(tmp[2]==1):
        vector=(tmp[0][0]-q[0],tmp[0][1]-q[1])
        di=(tmp[1][0]-tmp[0][0],tmp[1][1]-tmp[0][1])
        u_vector=[-vector[1],vector[0]]
        cos_theta=di[0]*u_vector[0]+di[1]*u_vector[1]
        #chekc it lie in clockwise or counter-clockwise direction
        if(cos_theta>0):
            u_vector[0]=-u_vector[0]
            u_vector[1]=-u_vector[1]
    if(tmp[2]==2):
        vector=(tmp[1][0]-q[0],tmp[1][1]-q[1])
        di=(tmp[1][0]-tmp[0][0],tmp[1][1]-tmp[0][1])
        u_vector=[-vector[1],vector[0]]
        cos_theta=di[0]*u_vector[0]+di[1]*u_vector[1]
        #chekc it lie in clockwise or counter-clockwise direction
        if(cos_theta>0):
            u_vector[0]=-u_vector[0]
            u_vector[1]=-u_vector[1]
    norm=mt.sqrt(u_vector[0]**2+u_vector[1]**2)
    n_vector=[]
    if(norm!=0):
        n_vector.append(u_vector[0]/norm)
        n_vector.append(u_vector[1]/norm)
        print("The unit-length vector u is:",n_vector)
    else:
        print("The point is on the boundary of the polygon.")
def checkPointInsidePolygon(q,mypolygon):
    if(q in mypolygon):
        print("The point is on the one of the vertices.")
        return False
    else:
        vertices_number=len(mypolygon)
        number_intersection=0
        for index in range(0,vertices_number):
            if(index!=vertices_number-1):
                d_min=min(mypolygon[index][0],mypolygon[index+1][0])
                d_max=max(mypolygon[index][0],mypolygon[index+1][0])
                if(q[0]<=d_max and q[0]>d_min):
                    (a,b,c)=computeLineThroughTwoPoints(mypolygon[index],mypolygon[index+1])
                    value_y=(-a*q[0]-c)/b
                    if(q[1]>=value_y):
                        number_intersection+=1
            else:
                d_min=min(mypolygon[index][0],mypolygon[0][0])
                d_max=max(mypolygon[index][0],mypolygon[0][0])
                if(q[0]<=d_max and q[0]>d_min):
                    (a,b,c)=computeLineThroughTwoPoints(mypolygon[index],mypolygon[0])
                    value_y=(-a*q[0]-c)/b
                    if(q[1]>=value_y):
                        number_intersection+=1
        if(number_intersection % 2 == 0):
            print("The point is not inside the polygon.")
            return True
        else:
            print("The point is inside the polygon.")
            return False
if __name__=='__main__':
    q=[3,4]
    mypolygon=[[0,0],[0,2],[2,2],[1,1],[2,0]]
    if(checkPointInsidePolygon(q,mypolygon)):
        tmp=computeDistancePointToPolygon(q,mypolygon)
        computeTangentVectorToPolygon(q,tmp)
        plt.scatter(q[0],q[1],s=10)
        polygon=plt.Polygon(mypolygon,fc="r")
        plt.gca().add_patch(polygon)
        plt.axis([-5,5,-5,5])
        plt.show()    
