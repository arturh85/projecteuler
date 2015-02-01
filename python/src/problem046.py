# coding=utf-8
'''
Problem 46
20 June 2003

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3 2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
----------------------------------------------------------
Created on 30.01.2015

@author: ahallmann
'''
import unittest
import timeit
import math

from problem042 import is_triangle_number
from problem042 import generate_triangle_numbers
from problem042 import generate_numbers
from problem042 import is_number
from problem044 import is_pentagonal_number

from problem003 import is_prime
from problem003 import generate_primes


def solve():
    i = 7.0
    while True:
        i += 2.0
        if is_prime(i):
            continue

        for prime in generate_primes():
            if prime > i:
                return i
            r = i - prime
            if not r % 2 == 0:
                continue

            r = math.sqrt(r / 2.0)
            if r == math.floor(r):
                break
    pass


class Test(unittest.TestCase):
    def test_sample(self):
        pass

    def test_answer(self):
        self.assertEqual(5777, solve())

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
# count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
