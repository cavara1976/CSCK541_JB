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



# New function calculating the shortest path using a recursive function
def shortestPath(i, j, k, d):
        #distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
        # Return weight when there are no intermediary vertices

        # base condition - no intermediate vertices are used
        if k == -1 or k <0:
         
            return (d[i][j])

        # If travelling via k is shorter return shorter distance
        else:
           
            #print (distance[i][j])
            return min(shortestPath(i, j, k-1, d),
                       shortestPath(i, k, k - 1,d) + shortestPath(k, j, k - 1,d))
         



def printSolution(distance):
    print("Following matrix shows the shortest distances between every pair of vertices: ")
    
    for start_node, end_node in itertools.product(range(MAX_LENGTH),
                                                  range(MAX_LENGTH)):
            if start_node == end_node:
                distance[start_node][end_node] = 0
                continue
         
            distance[start_node][end_node] = shortestPath(start_node,
                                                      end_node,
                                                      MAX_LENGTH-1, distance)
            print(distance)   
    return distance



# Driver's code
if __name__ == '__main__':

# Calls the function printSolution and passes the graph as an argument 
    print(printSolution(graph))

print("<<><><>><><><><><><><>")
print("Timeit Performance Test Result: ")
print (timeit.timeit())
print("<<><><>><><><><><><><>")

  