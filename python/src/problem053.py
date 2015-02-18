# coding=utf-8
'''
Problem 53
15 August 2003

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?
----------------------------------------------------------
Created on 18.02.2015

@author: ahallmann
'''
import unittest
import timeit
import math


def combination_count(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


def solve():
    cnt = 0
    for n in range(1, 101):
        for r in range(1, n+1):
            c = combination_count(n, r)
            if c > 1000000:
                cnt += 1
    return cnt

    
class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(10, combination_count(5, 3))
        self.assertEqual(1144066, combination_count(23, 10))
        pass

    def test_answer(self):
        self.assertEqual(4075, solve())
        pass

# -----------------------------------------


def run():
    return solve()


if __name__ == '__main__':
    run()
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
