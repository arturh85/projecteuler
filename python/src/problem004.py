'''
Problem 4
16 November 2001

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

----------------------------------------------------------
Created on 25.01.2012

@author: ahallmann
'''
import unittest
import timeit

def is_palindrome(numberString):
    return numberString == numberString[::-1]

'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def solve(digits):
    digitsRange = range(10**(digits-1),10**digits) 
    largest = 0

    for x in digitsRange:
        for y in digitsRange:
            val = x * y
            if val > largest and is_palindrome(str(val)):
                largest = val 
        
    return largest


class Test(unittest.TestCase):
    def testSimple(self):
        self.assertEqual(9, solve(1))
    def testSample(self):
        self.assertEqual(9009, solve(2))
    def testAnswer(self):
        self.assertEqual(906609, solve(3))
       
        
# -----------------------------------------

def run():
    solve(3)

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    