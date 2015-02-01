'''
Problem 35
17 January 2003

The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
----------------------------------------------------------
Created on 29.01.2015

@author: ahallmann
'''
import unittest
import timeit

from problem003 import generate_primes
from problem003 import is_prime

def rotations(number):
    s = str(number)
    for i in range(1, len(s)):
        s = s[1:] + s[:1]
        yield int(s)

def is_circular_prime(i):
    circular_primes_list = [i]
    for rotation in rotations(i):
        circular_primes_list.append(rotation)
        if not is_prime(rotation):
            return False
    return circular_primes_list

def circular_primes_below(limit):
    circular_primes = []
    for prime in generate_primes():
        p = is_circular_prime(prime)
        if prime > limit:
            break
        if p:
            circular_primes += p
    return set(circular_primes)

def solve():
    limit = 1000000
    circular_primes = circular_primes_below(limit)
    # print "there are " + str(len(circular_primes)) + " circular primes below " + str(limit)
    # circular_primes = list(circular_primes)
    # circular_primes.sort()
    # for prime in circular_primes:
    #     print prime
    return len(circular_primes)

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertFalse(is_circular_prime(23))
        self.assertTrue(is_circular_prime(197))
        self.assertEqual(13, len(circular_primes_below(100)))

    def test_answer(self):
        self.assertEqual(55, len(circular_primes_below(1000000)))
        pass
       
        
# -----------------------------------------

def run():
    return solve()

if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
