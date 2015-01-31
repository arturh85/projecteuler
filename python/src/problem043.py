'''
Problem 43
09 May 2003

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.

----------------------------------------------------------
Created on 30.01.2015

@author: ahallmann
'''
import unittest
import timeit
import itertools
import operator

from problem032 import generate_pandigital_numbers
from problem032 import is_pandigital
from problem003 import generate_primes


def has_problem_property(n):
    s = str(n)
    if len(s) == 9:
        s = '0' + s
    i = 1
    for prime in generate_primes():
        if prime > 17:
            return True
        part = int(s[i:i+3])
        if not part % prime == 0:
            return False
        i += 1

def solve():
    return sum(filter(has_problem_property, generate_pandigital_numbers(0, 9)))

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(has_problem_property(1406357289))
        self.assertFalse(has_problem_property(123456789))
        pass

    def test_answer(self):
        self.assertEqual(16695334890, solve())
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
