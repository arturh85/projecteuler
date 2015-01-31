'''
Problem 40
28 March 2003

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000

----------------------------------------------------------
Created on 30.01.2015

@author: ahallmann
'''
import unittest
import timeit
import itertools
import operator

from problem032 import is_pandigital


def generate_problem_fraction():
    i = 1
    while True:
        digits = list(str(i))
        for digit in digits:
            yield digit
        i += 1


def find_generated_values_at(generator, positions):
    i = 1
    last_position = max(positions)
    values = []
    for value in generator():
        if value is None:
            break
        if i in positions:
            values.append(value)
        i += 1
        if i > last_position:
            break
    return map(int, values)


def solve():
    return reduce(operator.mul, find_generated_values_at(generate_problem_fraction, [1, 10, 100, 1000, 10000, 100000, 1000000]))


class Test(unittest.TestCase):

    def test_sample(self):
        self.assertEqual([1], find_generated_values_at(generate_problem_fraction, [12]))
        self.assertEqual([1, 0, 1, 1], find_generated_values_at(generate_problem_fraction, [10, 11, 12, 13]))
        pass

    def test_answer(self):
        self.assertEqual(210, solve())
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
