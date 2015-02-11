'''
Problem 6
14 December 2001

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten 
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.

----------------------------------------------------------
Created on 25.01.2012

@author: ahallmann
'''
import unittest
import timeit

'''
Find the difference between the sum of the squares of the first one 
hundred natural numbers and the square of the sum.
'''
def solve(limit=100):
    sumSingle = 0
    sumSquared = 0
    
    for x in range(1, limit+1):
        sumSingle += x
        sumSquared += x*x
    
    return (sumSingle * sumSingle) - sumSquared

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2640, solve(10))
    def test_answer(self):
        self.assertEqual(25164150, solve())
       
        
# -----------------------------------------

def run():
    return solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    