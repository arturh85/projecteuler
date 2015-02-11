'''
Problem 5
30 November 2001

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?

----------------------------------------------------------
Created on 25.01.2012

@author: ahallmann
'''
import unittest
import timeit

'''
What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
'''
def solve(limit=20):
    i = limit
    divisors = range(limit-1, limit / 2, -1)
    while(True):
        i += limit
        allDivideable = True
        for x in divisors:
            if i % x != 0:
                allDivideable = False
                break
        
        if allDivideable:
            return i
    pass


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(2520, solve(10))
    def test_answer(self):
        self.assertEqual(232792560, solve())
        
       
        
# -----------------------------------------

def run():
    return solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    