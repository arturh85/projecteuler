'''
Problem 25
30 August 2002

The Fibonacci sequence is defined by the recurrence relation:


Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

----------------------------------------------------------
Created on 04.02.2012

@author: ahallmann
'''
import unittest
import timeit

from problem002 import fibonacci_sequence

def solve(over=1000):
    i = 1
    for x in fibonacci_sequence():
        if x >= over:
            return i
        i += 1
        
class Test(unittest.TestCase):        
    def testSample(self):
        self.assertEquals(100, 10**2)
        self.assertEquals(12, solve(10**2))
                             
    def testAnswer(self):
        self.assertEquals(4782, solve(10**999))
       
        
# -----------------------------------------

def run():
    solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    