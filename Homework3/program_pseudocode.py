Input: a graph G(m nodes) and a start point k(randomly selected)
Output: true->the graph is connected; false->the graph is disconnected
1.Create a parent node list P and insert k into this list
2.Create a parent node list P_store and insert k into this list
3.Create a child nodes list C
4.Create a Identity matrix(m*m) M
5.find all the nodes connected to k, and put them into a list, then insert the list into C
6.create a integer T, set it as 1
7.while(T!=0):
      T=0
      for each i in P:
          for each node j in C(i):
             if(j is not in P_store):
             if(M(i,j)!=0)  
                set M(i,j) and M(j,i) to 1
                find all the nodes connected to j and put them into a list, then insert the list into C
	  insert j into P_store
                insert j into P
                T+=1
          remove C(i) in C
          remove i in P
8.check whether the sum of all the entries in the matrix is equal to m*m or not:
9:yes->return true, no->return false

Input:the matrix M obtained from the part i.
output:the number of connected components and the number of nodes in each connected component
0.Create an empty list L
1.Set k equal to 0.
2.while(M is not an identity matrix):
3.  extract the columns and rows which contain 1s off the diagonal
4.  divide M into two smaller matrix.
5.  k+=1
6.  insert the size of the ones matrix into L
7.  set the smaller identity matrix as M
8   if(the size of M is 1*1):
        break;
9.  change the start point and implement the algorithm described in part i again
    
