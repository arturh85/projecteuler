'''
Problem 1
05 October 2001

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

----------------------------------------------------------
Created on 25.01.2012

@author: ahallmann
'''
import unittest
import timeit

'''
Find the sum of all the multiples of 3 or 5 below 1000.
'''
def solve(limit=1000):
    msum = 0
    
    for i in range(1, limit):
        if i % 3 == 0 or i % 5 == 0:
            msum += i
    
    return msum


class Test(unittest.TestCase):
    def testSample(self):
        self.assertEqual(23, solve(10))
    def testAnswer(self):
        self.assertEqual(233168, solve())
        
        
# -----------------------------------------

def run():
    solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    