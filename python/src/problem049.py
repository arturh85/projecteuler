# coding=utf-8
'''
Problem 49
18 July 2003

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
 is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers
  are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but
 there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
----------------------------------------------------------
Created on 01.02.2015

@author: ahallmann
'''
import unittest
import timeit
import itertools

from problem003 import is_prime
from problem003 import generate_primes
from problem032 import to_number

def primes_between(start, end):
    lst = []
    for prime in generate_primes():
        if prime > end:
            return lst
        if prime >= start:
            lst.append(prime)

def find_sequence(permutations):
    primes = filter(is_prime, permutations)
    if len(primes) < 3:
        return None
    primes.sort()

    for a in primes:
        for b in primes:
            for c in primes:
                if c >= b or b >= a:
                    continue
                if b - a == c - b:
                    result = [a, b, c]
                    result.sort()
                    return result
    return None


def solve():
    for prime in primes_between(1000, 10000):
        permutations = set(map(to_number, itertools.permutations(list(str(prime)))))
        sequence = find_sequence(permutations)
        if sequence:
            if 1487 not in sequence and 1063 not in sequence:
                return int(''.join(map(str, sequence)))

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual({1487, 4817, 8147}, set(find_sequence([1487, 4817, 8147])))
        pass

    def test_answer(self):
        self.assertEqual({2969, 6299, 9629}, set(find_sequence([2969, 6299, 9629])))
        self.assertEqual(296962999629, solve())
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
