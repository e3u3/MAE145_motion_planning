#A53307224
import math as mt
import numpy as np
def computeBFStree(adjtable,start_node):
    Q=[]
    parent=[]
    Q.append(start_node)
    number=len(adjtable)
    none=-1
    for i in range(1,number+1):
        parent.append(none)
    parent[start_node-1]=start_node
    while(len(Q)!=0):
        v=Q.pop()
        child_node=adjtable[v-1]
        for u in child_node:
            if(parent[u-1]==none):
                parent[u-1]=v
                Q.append(u)
    if(-1 in parent):
        print("The graph is disconnected!")
    else:
        print("The graph is connected!")
        print("Here is the vector of pointers describing the BFS tree rooted as start:")
        print(parent)
    return parent

def computeBFSpath(adjtable,start_node,goal_node):
    Q=[]
    parent=[]
    Q.append(start_node)
    number=len(adjtable)
    none=-1
    for i in range(1,number+1):
        parent.append(none)
    parent[start_node-1]=start_node
    while(len(Q)!=0):
        v=Q.pop()
        child_node=adjtable[v-1]
        for u in child_node:
            if(parent[u-1]==none):
                parent[u-1]=v
                Q.append(u)
            if(u==goal_node):
                return parent
    if(-1 in parent):
        print("The graph is disconnected!")
    else:
        print("The graph is connected!")
        print("Here is the vector of pointers describing the BFS tree rooted as start:")
        print(parent)
    return parent
def extractPath(parent,goal_node,start_node):
    P=[]
    P.insert(0,goal_node)
    parent_node=parent[goal_node-1]
    P.insert(0,parent_node)
    while(parent_node!=start_node):
        parent_node=parent[parent_node-1]
        P.insert(0,parent_node)
    return P
if __name__=='__main__':
    start_node=1
    goal_node=32
    number_nodes=32
    Adjtable=[]
    for i in range(0,number_nodes):
        Adjtable.append(0)
    Adjtable[0]=[2,6]
    Adjtable[1]=[1,3,7]
    Adjtable[2]=[2,4,8]
    Adjtable[3]=[3,5,9]
    Adjtable[4]=[4,10]
    Adjtable[5]=[1,7,11]
    Adjtable[6]=[2,6,8]
    Adjtable[7]=[3,7,9]
    Adjtable[8]=[4,8,10]
    Adjtable[9]=[5,9,12]
    Adjtable[10]=[6,13]
    Adjtable[11]=[10,14]
    Adjtable[12]=[11,15]
    Adjtable[13]=[12,17]
    Adjtable[14]=[13,16,18]
    Adjtable[15]=[15,19]
    Adjtable[16]=[14,20]
    Adjtable[17]=[15,19,21]
    Adjtable[18]=[16,18,22]
    Adjtable[19]=[17,25]
    Adjtable[20]=[18,22,26]
    Adjtable[21]=[19,21,23]
    Adjtable[22]=[22,24]
    Adjtable[23]=[23,25]
    Adjtable[24]=[20,24,27]
    Adjtable[25]=[21,28]
    Adjtable[26]=[25,32]
    Adjtable[27]=[26,29]
    Adjtable[28]=[28,30]
    Adjtable[29]=[29,31]
    Adjtable[30]=[30,32]
    Adjtable[31]=[27,31]
    #computeBFStree(Adjtable,2)
    path=computeBFSpath(Adjtable,start_node,goal_node)
    print(path)
    P=extractPath(path,goal_node,start_node)
    print(P)
