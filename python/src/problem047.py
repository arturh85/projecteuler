# coding=utf-8
'''
Problem 47
04 July 2003

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
----------------------------------------------------------
Created on 30.01.2015

@author: ahallmann
'''
import unittest
import timeit

from problem003 import prime_factors

def check_problem_property(numbers):
    number_factors = map(prime_factors, numbers)
    # print numbers, "factors", number_factors
    mem = []
    i = 0
    for factors in number_factors:
        if len(factors) == 0:
            return False
        if len(factors) != len(numbers):
            return False
        for factor in factors:
            if factor in mem:
                return False
            mem.append(factor)
        i += 1
    return True


# FIXME: too slow! 81s for n=4
def solve(n=4):
    i = 0
    while True:
        i += 1
        consecutive_numbers = range(i, i + n)
        if check_problem_property(consecutive_numbers):
            return i


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual([2, 7], prime_factors(14))
        self.assertEqual([3, 5], prime_factors(15))

        self.assertEqual([4, 7, 23], prime_factors(644))
        self.assertEqual([3, 5, 43], prime_factors(645))
        self.assertEqual([2, 17, 19], prime_factors(646))

        self.assertTrue(check_problem_property([14, 15]))
        self.assertTrue(check_problem_property([644, 645, 646]))
        self.assertTrue(check_problem_property([134043, 134044, 134045, 134046]))
        self.assertTrue(check_problem_property([238203, 238204, 238205, 238206]))

    def test_answer(self):
        self.assertEqual(14, solve(2))
        self.assertEqual(644, solve(3))
        # self.assertEqual(134043, solve(4))
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
