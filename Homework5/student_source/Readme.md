This is a template file on which you can build an RRT planner. You
need to edit the planner function in the RRT class to make your
planner work.  You can add functions to your class or other functions
as you choose. You are given two files main.py and
auxiliary_functions.py.  Currently, the code doesn't work but if you
run the main.py function you will see random movement from the start
node to random nodes.

You have to do four main tasks:
# Task 1: Find the nearest node in the tree to the sampled point
# Task 2: Find the distance to that node and if the distance is greater than 
#         0.25; use the logic mentioned in the question to find the new point.
# Task 3: Check if the new point connects to the tree you are building
#         without hitting an obstacle. You can use the auxiliary function
#         to do this. You might want to tweak the parameters to sample the
#         line segment.
# Task 4: If you can connect the tree to the new point by a collision-free path, 
#         make this point a node in the tree with its parent as the nearest node
#         to the tree.


There are two classes created:

1. RRT: This class implements the RRT
planner and the drawing of the RRT in the workspace. The class knows
the start point, the goal point, obstacle list and a list of nodes in the
RRT tree

2. Node: This class has three parameters. The x, y positions and the
node index of the parent. The index is the location of the parent in
the node list in the RRT class.

You can define your obstacles and start and goal in the main.py
file. A suggestion is  that you leave everything in their current
setting and focus on implementing the planner. You should edit the
planner function to include the rules for RRT and also check for
collisions with obstacles.  Please note defining the obstacles have to
be in the anticlockwise direction of the vertices if you choose to add
obstacles.

Libraries required:
numpy
matplotlib
math
copy

Most of these libraries have already been used in your previous HW so
you don't have to install them.