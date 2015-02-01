'''
Problem 9
25 January 2002

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

----------------------------------------------------------
Created on 26.01.2012

@author: ahallmann
'''
import unittest
import timeit
import math


def is_pythagorean_triplet(a,b,c):
    return int(a*a) + int(b*b) == int(c*c)

def solve(tripletSum):
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = math.sqrt(a*a + b*b)
            
            #print "a = " + str(a) + " b = " + str(b) + " c = " + str(c)
            
            if a+b+c == tripletSum:
                return int(a*b*c)
        
    return None

class Test(unittest.TestCase):
    def testSimple0(self):
        self.assertTrue(is_pythagorean_triplet(1,1,math.sqrt(2)))
    def testSimple1(self):
        self.assertTrue(is_pythagorean_triplet(3,4,5))
    def testSimple2(self):
        self.assertFalse(is_pythagorean_triplet(3,4,6))
    def testAnswer(self):
        self.assertEqual(31875000, solve(1000))
       
        
# -----------------------------------------

def run():
    return solve(1000)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    