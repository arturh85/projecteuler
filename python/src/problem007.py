'''
Problem 7
28 December 2001

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?


----------------------------------------------------------
Created on 25.01.2012

@author: ahallmann
'''
import unittest
import timeit
from problem003 import generate_primes

def prime_at(nr):
    prime_nr = 1
    for prime in generate_primes():
        if prime_nr == nr:
            return prime
        prime_nr += 1

class Test(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(2, prime_at(1))
    def test_simple2(self):
        self.assertEqual(3, prime_at(2))
    def test_sample(self):
        self.assertEqual(13, prime_at(6))
    def test_answer(self):
        self.assertEqual(104743, prime_at(10001))
       
        
# -----------------------------------------

def run():
    return prime_at(10001)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    