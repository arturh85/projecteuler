# coding=utf-8
"""
Problem 56
07 November 2013

A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large:
one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
----------------------------------------------------------
Created on 19.02.2015

@author: ahallmann
"""
import unittest
import timeit


def solve():
    max_sum = 0
    for a in range(100):
        for b in range(100):
            v = a ** b
            s = sum(map(int, list(str(v))))
            if s > max_sum:
                max_sum = s
    return max_sum


class Test(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(972, solve())
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
