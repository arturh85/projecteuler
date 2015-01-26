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
Created on 11.02.2012

@author: ahallmann
'''
import unittest
import timeit
import sys
from problem003 import is_prime

from decimal import *
def precise_quotient(numerator, denominator, prec):
    getcontext().prec = prec + 10
    return str(Decimal(numerator) / Decimal(denominator))[0:(prec+2)]

def longest_recurring_cycle(s, debug=False):
    for prefix_length in range(len(s)-1):
        length = len(s) - prefix_length
        for cycle_length in xrange(1, (length / 2)+1):
            success = True
            for i in xrange(length):
                if s[prefix_length + i] != s[prefix_length + (i % cycle_length)]:
                    success = False
                    break
            if success:
                if debug:
                    print("cycle found '" + s[prefix_length:(prefix_length + cycle_length)] + "' @ " + s)
                return cycle_length
    return 0

def solve(limit=1000, prec=50, debug=False):
    longest = 0
    longest_i = 0
    primes = [2]

    for i in xrange(2, limit + 1):
        if debug and i % 10 == 0:
            print ".",
            sys.stdout.flush()
        if is_prime(i, primes):
            num = precise_quotient(1, i, prec)
            length = longest_recurring_cycle(num.replace("0.", ""))
            if length > longest:
                longest = length
                longest_i = i
    if debug:
        print("")
        print("longest: 1/" + str(longest_i) + " with len = " + str(longest))
    return longest

def test(numerator, denominator, prec=50, debug=False):
    num = precise_quotient(numerator, denominator, prec)
    return longest_recurring_cycle(num.replace("0.", ""), debug)

class Test(unittest.TestCase):
    def test_longest_recurring_cycle(self):
        self.assertEquals(0, longest_recurring_cycle("1"))
        self.assertEquals(0, longest_recurring_cycle("10"))
        self.assertEquals(1, longest_recurring_cycle("11"))
        self.assertEquals(1, longest_recurring_cycle("1111111111"))
        self.assertEquals(1, longest_recurring_cycle("01111111111"))
        self.assertEquals(2, longest_recurring_cycle("12121212"))
        self.assertEquals(3, longest_recurring_cycle("123123"))
        self.assertEquals(96, test(1, 97, 10000)) # from en.wikipedia.org/wiki/Repeating_decimal

    def test_precise_quotient(self):
        self.assertEquals("0.333333333333", str(1.0/3.0))
        self.assertEquals("0.33", precise_quotient(1, 3, 2))
        self.assertEquals("0.3333333333333333", precise_quotient(1, 3, 16))
        self.assertEquals("0.33333333333333333", precise_quotient(1, 3, 17))

    def test_sample(self):
        self.assertEquals(0, test(1, 2)) # 1/2  = 0.5
        self.assertEquals(1, test(1, 3)) # 1/3  = 0.(3)
        self.assertEquals(0, test(1, 4)) # 1/4  = 0.25
        self.assertEquals(0, test(1, 5)) # 1/5  = 0.2
        self.assertEquals(1, test(1, 6)) # 1/6  = 0.1(6)
        self.assertEquals(6, test(1, 7)) # 1/7  = 0.(142857)
        self.assertEquals(0, test(1, 8)) # 1/8  = 0.125
        self.assertEquals(1, test(1, 9)) # 1/9  = 0.(1)
        self.assertEquals(0, test(1,10)) # 1/10 = 0.1
        self.assertEquals(6, solve(10))

    def test_edge_case(self):
        self.assertEquals("0.14285714285", precise_quotient(1, 7, 11))
        self.assertEquals("0.142857142857", precise_quotient(1, 7, 12))
        self.assertEquals(0, test(1, 7, 11)) # 1/7  = 0.(142857)
        self.assertEquals(6, test(1, 7, 12)) # 1/7  = 0.(142857)

    def test_debug(self):
        #self.assertEquals(6, test(1, 7, 100000))
        #self.assertEqual(24, test(1, 511, 100000))
        #self.assertEqual(24, test(1, 511, 100000))
        #self.assertEqual(24, test(1, 511, 100000))
        #self.assertEqual(50, test(1, 251, 100000))
        #self.assertEqual(75, test(1, 151, 100000))
        #self.assertEqual(99, test(1, 199, 100000))
        #self.assertEqual(300, test(1, 601, 10000))
        #self.assertEqual(498, test(1, 499, 100000))
        #self.assertEqual(982, test(1, 983, 100000))
        pass

    def test_answer(self):
        #self.assertEqual(24, solve(1000, 50, True))
        #self.assertEqual(50, solve(1000, 100, True))
        #self.assertEqual(75, solve(1000, 150, True))
        #self.assertEqual(99, solve(1000, 200, True))
        #self.assertEqual(99, solve(1000, 300, True))
        #self.assertEqual(99, solve(1000, 600, True))
        #self.assertEqual(498, solve(1000, 1000, True))
        #self.assertEqual(982, solve(1000, 2000, True)) # 23 s
        #self.assertEqual(982, solve(1000, 3000, True)) # 47 s
        pass
       
        
# -----------------------------------------

def run():
    solve(1000, 2000, True) # 23 s

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
