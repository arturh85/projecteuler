'''
Problem 26
13 September 2002

A unit fraction contains 1 in the numerator. The decimal representation 
of the unit fractions with denominators 2 to 10 are given:

    1/2    =     0.5
    1/3    =     0.(3)
    1/4    =     0.25
    1/5    =     0.2
    1/6    =     0.1(6)
    1/7    =     0.(142857)
    1/8    =     0.125
    1/9    =     0.(1)
    1/10    =     0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest 
recurring cycle in its decimal fraction part.

----------------------------------------------------------
Created on 04.02.2012

@author: ahallmann
'''
import unittest
import timeit

def longest_recurring_cycle(s):
    return 1


def solve(limit=1000):
    longest = 0
    longest_i = 0
    for i in range(2, limit):
        s = str(1.0/i)
        
        l = longest_recurring_cycle(s)
        
        if l > longest:
            longest = l
            longest_i = i
            
    return longest_i


class Test(unittest.TestCase):        
    def testSample(self):
        pass
                             
    def testAnswer(self):
        pass
       
        
# -----------------------------------------

def run():
    solve(10)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    