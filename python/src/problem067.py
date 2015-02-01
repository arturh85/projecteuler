'''
Problem 67
09 April 2004

By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt 
(right click and 'Save Link/Target As...'), a 15K text file containing 
a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible 
to try every route to solve this problem, as there are 2^99 altogether! If 
you could check one trillion (10^12) routes every second it would take over 
twenty billion years to check them all. There is an efficient algorithm 
to solve it. ;o)


----------------------------------------------------------
Created on 31.01.2012

@author: ahallmann
'''
import unittest
import timeit

from problem018 import max_sum_route

triangle_1 = [
       [3],
      [7, 4],
     [2, 4, 6],
    [8, 5, 9, 3],
]

def read_triangle(filename):
    f = open(filename, 'r')
    triangle = []
    for line in f.readlines():
        values = []
        for value in line.split(" "):
            values.append(int(value))
        
        triangle.append(values)

    f.close()
    return triangle

triangle_2 = read_triangle("data/problem067.txt")

class Test(unittest.TestCase):        
    def testSample(self):
        self.assertEqual(23, max_sum_route(triangle_1, 1))
        self.assertEqual(23, max_sum_route(triangle_1, 2))
                                 
    def testAnswer(self):
        self.assertEqual(7269, max_sum_route(triangle_2, 78))
        self.assertEqual(7273, max_sum_route(triangle_2, 79))
        self.assertEqual(7273, max_sum_route(triangle_2, 90))
        self.assertEqual(7273, max_sum_route(triangle_2, 100))
       
        
# -----------------------------------------

def run():
    return max_sum_route(triangle_2, 79)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 100
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    