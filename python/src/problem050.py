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

from problem049 import primes_between


def solve(n=1000000):
    primes = primes_between(1, n)
    prime_count = len(primes)
    most_consecutive_primes = 1
    most_consecutive_primes_nr = 0
    for i in range(0, 4):
        for l in range(most_consecutive_primes, n-i):
            if i+l > prime_count:
                continue
            m = primes[i:i+l]
            s = sum(m)
            if s > n: 
                break
            if s in primes:
                most_consecutive_primes = l
                most_consecutive_primes_nr = s
    return most_consecutive_primes_nr
    
    
class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(41, solve(100))
        self.assertEqual(953, solve(1000))
        pass

    def test_answer(self):
        self.assertEqual(997651, solve(1000000))
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
