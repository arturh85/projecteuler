'''
Problem 20
21 June 2002

n! means n x (n - 1) x ... x 3 x 2 x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

----------------------------------------------------------
Created on 31.01.2012

@author: ahallmann
'''
import unittest
import timeit
import math

def factorial_sum(n):
    fsum = 0
    
    for character in str(math.factorial(n)):
        fsum += int(character)
      
    return fsum


class Test(unittest.TestCase):        
    def testSample(self):
        self.assertEqual(27, factorial_sum(10))
                                 
    def testAnswer(self):
        self.assertEqual(648, factorial_sum(100))
        pass
       
        
# -----------------------------------------

def run():
    factorial_sum(100)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    