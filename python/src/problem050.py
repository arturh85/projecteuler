# coding=utf-8
'''
Problem 50
15 August 2003

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
----------------------------------------------------------
Created on 01.02.2015

@author: ahallmann
'''
import unittest
import timeit
import itertools

from problem003 import is_prime
from problem049 import primes_between


def solve(n=1000000):
    primes = primes_between(1, n)
    most_consecutive_primes = 1
    most_consecutive_primes_set = 1
    most_consecutive_primes_nr = 0
    for i in range(0, n):
        for l in range(most_consecutive_primes, n):
            m = primes[i:l]
            if len(m) != l:
                continue
            s = sum(m)
            if s < n and is_prime(s):
                print "goal", i, l, m, s
                most_consecutive_primes = l
                most_consecutive_primes_nr = s
                most_consecutive_primes_set = m
    print most_consecutive_primes_nr, "with", most_consecutive_primes, "primes", most_consecutive_primes_set
    return most_consecutive_primes_nr
    
    
class Test(unittest.TestCase):
    def test_sample(self):
        # self.assertEqual(41, solve(100))
        self.assertEqual(953, solve(1000))
        pass

    def test_answer(self):
        # self.assertEqual({2969, 6299, 9629}, set(find_sequence([2969, 6299, 9629])))
        pass

# -----------------------------------------

def run():
    raise Exception("not finished ...")


if __name__ == '__main__':
    run()
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
