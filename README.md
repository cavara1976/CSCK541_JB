# CSCK541_JB
Python Programming Assignment

This is an example of a recursive approach to the Floyd Warshall algorithm that was devised from an iterative solution.

Getting Started:

Please install necessary packages that can be found in requirements.txt.
Install the requirements .txt file by entering the following into your shell/command line terminal: pip install -r requirements.txt.

To execute the code: change the directory to src folder and  excecute then following:

$ ./floyd.resursive_final

$ ./floyd.imperative_final

Output:

After running the recursive and imperative programs in your terminal you should see the following results:

[[0, 7, 12, 8], [9223372036854775807, 0, 5, 7], [9223372036854775807, 9223372036854775807, 0, 2], [9223372036854775807, 9223372036854775807, 9223372036854775807, 0]]


<<><><>><><><><><><><>
Timeit Performance Test Result: 
0.005245162999999999
<<><><>><><><><><><><>

Tests:

This code runs performances tests using Python's timeit function in the floyd_imperative_final and floyd_resursive_final source code files.
A separate unit test file has been included to test the recursive version of the algorithm.

Licence:

Copyright 2023 Jonathan Brome
