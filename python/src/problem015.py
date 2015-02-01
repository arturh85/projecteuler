'''
Problem 15
19 April 2002

Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?

----------------------------------------------------------

    2x2:
    0011
    0110
    1100
    0101
    1010
    1001
       
    
    3x3:
    000111
    001101
    111000
    101100
    100110
    
    ...    

----------------------------------------------------------
Created on 30.01.2012

@author: ahallmann
'''
import unittest
import timeit
import math

def solve(gridsize):
    n = 2 * gridsize
    k = gridsize
    
    return binomial_coefficient(n, k)

def binomial_coefficient(n, k): 
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k)) 

class Test(unittest.TestCase):
    def testSample(self):
        self.assertEqual(6, solve(2))
    def testSample2(self):
        self.assertEqual(20, solve(3))
    def testAnswer(self):
        self.assertEqual(137846528820, solve(20))
       
        
# -----------------------------------------

def run():
    return solve(20)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    