# coding=utf-8
'''
Problem 44
09 May 2003

Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
and D = |Pk − Pj| is minimised; what is the value of D?
----------------------------------------------------------
Created on 30.01.2015

@author: ahallmann
'''
import unittest
import timeit

from problem042 import generate_numbers
from problem042 import is_number


def pentagonal_numbers_at(n):
    return n * (3 * n - 1) / 2


def generate_pentagonal_numbers():
    return generate_numbers(pentagonal_numbers_at)


def is_pentagonal_number(n):
    return is_number(pentagonal_numbers_at, 'pentagonal', n)


def solve():
    min_distance = 999999
    for a in range(1, 10000):
        for b in range(1, 10000):
            if a == b:
                continue
            c = pentagonal_numbers_at(a)
            d = pentagonal_numbers_at(b)

            p_sum = c + d
            p_distance = abs(c - d)

            # print "c " + str(c)
            # print "d " + str(d)

            if is_pentagonal_number(p_sum) and is_pentagonal_number(p_distance):
                min_distance = p_distance

                break

    return min_distance


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(22, pentagonal_numbers_at(4))
        self.assertEqual(70, pentagonal_numbers_at(7))
        self.assertEqual(92, pentagonal_numbers_at(8))

        self.assertTrue(is_pentagonal_number(92))
        pass

    def test_answer(self):
        self.assertEqual(42, solve())
        pass


# -----------------------------------------

def run():
    solve()
    pass


if __name__ == '__main__':
    run()
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
