

import sys
import itertools


NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8],
         [NO_PATH, 0, 5, NO_PATH],
         [NO_PATH, NO_PATH, 0, 2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])



# New function calculating the shortest path using a recursive function
def shortestPath(i, j, k):
        #distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
        # Return weight when there are no intermediary vertices

        # base condition - no intermediate vertices are used
        if k == -1:
            return 

        # If travelling via k is shorter return shorter distance
        else:
            return min(shortestPath(i, j, k-1),
                       shortestPath(i, k, k - 1) + shortestPath(k, j, k - 1))
     
def printSolution(distance):
    print("Following matrix shows the shortest distances between every pair of vertices")
    
    for start_node, end_node in itertools.product(range(MAX_LENGTH),
                                                  range(MAX_LENGTH)):
        # Assumes that if start_node and end_node are the same
        # then the distance would be zero
        for start_node, end_node in itertools.product(range(MAX_LENGTH),
                                                  range(MAX_LENGTH)):
         
            distance[start_node][end_node] = shortestPath(start_node,
                                                      end_node,
                                                      MAX_LENGTH-1)
                
    return distance

if __name__ == '__main__':
    # Calls the function floyd and passes the definition of graph
    print(printSolution(graph))