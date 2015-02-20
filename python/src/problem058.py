# coding=utf-8
"""
Problem 58
05 December 2013

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
----------------------------------------------------------
Created on 19.02.2015

@author: ahallmann
"""
import unittest
import timeit
import sys

from problem003 import is_prime
from problem028 import spiral
from fractions import Fraction
from problem049 import primes_between


cache = {}

def diagonals(n):
    if n <= 0:
        return ([1], []);
    if n in cache:
        return cache[n]
    o, p = diagonals(n-1)
    o = o[:] # copy cached list
    p = p[:] # copy cached list
    for i in range(4):
        u = o[-1] + n * 2
        if is_prime(u):
            p.append(u)
        o.append(u)
    result = (o, p)
    cache[n] = result
    return result


def ratio(n, d):
    return 100 * float(n) / float(d)
    
    
def solve():
    i = 1
    while True:
        d, p = diagonals(i)
        r = ratio(len(p), len(d))
        if r < 10:
            return 1 + i * 2
        i += 1


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(17, len(diagonals(4)[0]))
        self.assertEqual(13, len(diagonals(3)[0]))
        self.assertEqual(8, len(filter(is_prime, diagonals(3)[0])))
        self.assertEqual(62, round(ratio(8, 13), 0))
        pass
        
    def test_answer(self):
        self.assertEqual(26241, solve())
        pass


# -----------------------------------------


def run():
    return solve()


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
