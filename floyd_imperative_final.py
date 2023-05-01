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

#This function implements the imperative version of the Floyd Marshal algorithm using iteration

def floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH),
                         range(MAX_LENGTH)):

        # Assume that distance is zero if tart_node == end_node 
      
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # find the minimum distance and return the path result
        distance[start_node][end_node] = min(distance[start_node][end_node],distance[start_node][intermediate] +
                                             distance[intermediate][end_node])

    # Print the distance
    print(distance)


# Driver's code
if __name__ == '__main__':

# Calls the function floyd and passes the graph as an argument 
    floyd(graph)

print("<<><><>><><><><><><><>")
print("Timeit Performance Test Result: ")
print (timeit.timeit())
print("<<><><>><><><><><><><>")


