#!/usr/bin/env python3
import unittest
import sys
from floyd_recursive_final import printSolution
from floyd_imperative_final import floyd
NO_PATH = sys.maxsize


# Test the printSolution and floyd functions in the recursive and imperative function
class OutputTest(unittest.TestCase):

    def test_floyd_function(self):

        def setUp(self) -> None:
                pass
        def tearDown(self) -> None:
                 pass

        def test_shortestPath(self) -> None:

            graph_new = [[0, 7, NO_PATH, 8],
                        [NO_PATH, 0, 5, NO_PATH],
                        [NO_PATH, NO_PATH, 0, 2],
                        [NO_PATH, NO_PATH, NO_PATH, 0]]

            result = printSolution(graph_new)
            result2 = floyd(graph_new)
        
            self.assertEqual(result, [[0, 7, 12, 8],
                                [NO_PATH    , 0, 5, 7],
                                [NO_PATH , NO_PATH , 0, 2],
                                [NO_PATH , NO_PATH , NO_PATH , 0]
                             ])
            self.assertEqual(result2, [[0, 7, 12, 8],
                                [NO_PATH    , 0, 5, 7],
                                [NO_PATH , NO_PATH , 0, 2],
                                [NO_PATH , NO_PATH , NO_PATH , 0]
                             ])


            printSolution(graph_new)

  
# Driver's code
    
    if __name__== "__main__":
        graph_new =[[0, 7, NO_PATH , 8],
            [NO_PATH , 0, 5, NO_PATH ],
             [NO_PATH , NO_PATH, 0, 2],
            [NO_PATH , NO_PATH , NO_PATH , 0]
    ]
    unittest.main()
