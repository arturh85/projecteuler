# coding=utf-8
'''
Problem 45
06 June 2003

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
----------------------------------------------------------
Created on 30.01.2015

@author: ahallmann
'''
import unittest
import timeit

from problem042 import is_triangle_number
from problem042 import generate_triangle_numbers
from problem042 import generate_numbers
from problem042 import is_number
from problem044 import is_pentagonal_number


def hexagonal_number_at(n):
    return n * (2 * n - 1)


def generate_hexagonal_number():
    return generate_numbers(hexagonal_number_at)


def is_hexagonal_number(n):
    return is_number(hexagonal_number_at, 'hexagonal', n)


# FIXME: way to slow, 88s
def solve():
    for triangle_number in generate_triangle_numbers():
        if triangle_number > 40755 and is_pentagonal_number(triangle_number) and is_hexagonal_number(triangle_number):
            return triangle_number

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(is_pentagonal_number(40755))
        self.assertTrue(is_triangle_number(40755))
        self.assertTrue(is_hexagonal_number(40755))
        pass

    def test_answer(self):
        self.assertEqual(1533776805, solve())
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
