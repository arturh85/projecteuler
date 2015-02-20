# coding=utf-8
"""
Problem 57
21 November 2013

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example 
where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
----------------------------------------------------------
Created on 19.02.2015

@author: ahallmann
"""
import unittest
import timeit
import sys
from fractions import Fraction

cache = {}

def converge_square_2(n, x=1):
    if n <= 0:
        return x
    if x == 2 and n in cache:
        return cache[n]
    result = x + Fraction(1, converge_square_2(n-1, 2))
    if x == 2:
        cache[n] = result
    return result


def solve(n=1000):
    cnt = 0
    for n in range(1, n+1):
        f = converge_square_2(n)
        if len(str(f.numerator)) > len(str(f.denominator)):
            cnt += 1
    return cnt


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(Fraction(1, 1), converge_square_2(0))
        self.assertEqual(Fraction(3, 2), converge_square_2(1))
        self.assertEqual(Fraction(7, 5), converge_square_2(2))
        self.assertEqual(Fraction(17, 12), converge_square_2(3))
        self.assertEqual(Fraction(41, 29), converge_square_2(4))
        self.assertEqual(Fraction(99, 70), converge_square_2(5))
        self.assertEqual(Fraction(239, 169), converge_square_2(6))
        self.assertEqual(Fraction(577, 408), converge_square_2(7))
        self.assertEqual(Fraction(1393, 985), converge_square_2(8))
        
        self.assertEqual(1, solve(10))
        
    def test_answer(self):
        self.assertEqual(153, solve())


# -----------------------------------------


def run():
    return solve()


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
