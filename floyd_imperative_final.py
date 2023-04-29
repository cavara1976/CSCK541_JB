#!/usr/bin/env python3
import sys
import itertools
import timeit

NO_PATH = sys.maxsize

global graph
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH: int = len(graph[0])

#This function implements the iterative version of the Floyd Marshal algorithm

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH),
                         range(MAX_LENGTH)):

        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],distance[start_node][intermediate] +
                                             distance[intermediate][end_node])

    # Any value that have sys.maxsize has no path
    print(distance)


# Driver's code
if __name__ == '__main__':

# Calls the function printSolution and passes the graph as an argument 
    floyd(graph)

print("<<><><>><><><><><><><>")
print("Timeit Performance Test Result: ")
print (timeit.timeit())
print("<<><><>><><><><><><><>")


