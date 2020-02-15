# Include here your student identification number e.g. A123456
import matplotlib.pyplot as plt
import numpy as np
from auxiliary_functions import inCollision

# node class which has the x and y position along with the parent
# node index
class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

# RRT class implementation
class RRT():
    def __init__(self, start, goal, obstacle_list):
        self.start = Node(start[0], start[1])  # start node for the RRT
        self.goal = Node(goal[0], goal[1])     # goal node for the RRT
        self.obstacle_list = obstacle_list     # list of obstacles 
        self.node_list = []    # list of nodes added while creating the RRT

# You need to complete this planning part of the code, note that it has a
# random sampling part that outputs a random_point, but still you need
# to try to connect this random_point to the tree, by finding the
# closest node, and verify that the segment connecting to the tree
# is collision free. To check for collisions use an imported auxiliary
# function.

# Task 1: Find the nearest node to the sampled point

# Task 2: Find the distance to that node and if distance is greater than 
#         0.25 use logic mentioned in the question to find the new point.

# Task 3: Check if the new point connects to the tree you are building
#         without hitting an obstacle. You can use the auxiliary function
#         to do this.

# Task 4: If collision free from the tree to the new point. Make this
#         point a node in the tree with its parent as the nearest node
#         to the tree.

    def planning(self, animation=True):
        self.node_list = [self.start]
        while self.goal.parent is None:
            # Random Sampling
            # We are choosing the goal node with 0.1 probability, this
            # gives a bias to RRT to search towards the goal. Increasing
            # the bias may take longer time to converge to goal if the 
            # path has lot of obstacles in its path. Tune this parameter to
            # see the differences 
            if np.random.rand() > 0.1:
                random_point = np.random.sample((2, 1))*10.1
            else:
                random_point = np.asarray([self.goal.x, self.goal.y],
                                          dtype=float)
            # creating a node from the point
            new_node = Node(random_point[0], random_point[1])
            # set the parent as index no of the node in the self.node_list
            new_node.parent = 0 # setting the parent of new node to start node 
                                # as 0 refers to the first node in self.node_list
            self.node_list.append(new_node) # storing the nodes in a list

            if animation:
                self.drawGraph(random_point)
        # once the goal node has a parent this means the tree has a path
        # to the start node.
        # Edit below this line at your own risk. This will take care of creating a
        # path from goal to start.
        path = [[self.goal.x, self.goal.y]]
        prev_node_index = len(self.node_list) - 1
        while self.node_list[prev_node_index].parent is not None:
            node = self.node_list[prev_node_index]
            path.append([node.x, node.y])
            prev_node_index = node.parent
        path.append([self.start.x, self.start.y])

        return path

    # input: node as defined by node class
    # input: point defined as a list (x,y)
    # output: distance between the node and point
    def calcDistNodeToPoint(self, node, point):
        # TODO: implement a method to calculate distance
        return 0

    # input: random_point which you sampled as (x,y)
    # output: index of the node in self.node_list
    def getNearestNode(self, random_point):
        # TODO: implement a method to find the closest node to the random_point
        index = 0 # delete after implementation
        return index

    # edit this function at your own risk 
    def drawGraph(self, random_point=None):
        plt.clf()
        # draw random point
        if random_point is not None:
            plt.plot(random_point[0], random_point[1], "^k")
        # draw the tree
        for node in self.node_list:
            if node.parent is not None:
                plt.plot([node.x, self.node_list[node.parent].x], [
                         node.y, self.node_list[node.parent].y], "-g")
        # draw the obstacle
        for obstacle in self.obstacle_list:
            obstacle_draw = plt.Polygon(obstacle, fc="b")
            plt.gca().add_patch(obstacle_draw)
        # draw the start and goal points
        plt.plot(self.start.x, self.start.y, "xr")
        plt.plot(self.goal.x, self.goal.y, "xr")
        plt.axis([0, 10, 0, 10])
        plt.grid(True)
        plt.pause(0.01)

# You can define any other methods in for the rrt object (i.e. functions
# that apply to the rrt object attributes) and which can help you
# complete the assignment, for example to obtain q nearby


if __name__ == '__main__':
    # Define obstacle polygon in the counter clockwise direction
    obstacle_list = [[[3, 3], [4, 3], [4, 4], [3, 4]],
                     [[8, 8], [7, 6], [9, 9]]]
    # Set Initial parameters
    rrt = RRT(start=[2, 2], goal=[5, 5], obstacle_list=obstacle_list)
    show_animation = True
    path = rrt.planning(animation=show_animation)
    # Draw final path
    if show_animation:
        rrt.drawGraph()
        plt.plot([x for (x, y) in path], [y for (x, y) in path], '-r')
        plt.grid(True)
        plt.show()
