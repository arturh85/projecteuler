'''
Problem 3
02 November 2001

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

----------------------------------------------------------
Created on 25.01.2012

@author: ahallmann
'''
import unittest
import timeit
import math

'''
checks whether a number is prime.
if a list of previous primes is given as a parameter
the performance is greatly increased
'''
def is_prime(number, primes=None):
    if number < 2: return False
    
    i = 2
    limit = int(math.sqrt(number))

    if primes == None:
        while i <= limit:
            if number % i == 0:
                return False
            i += 1
    else:
        for x in primes:
            if x > limit: return True
        
            if number % x == 0:
                return False
        
    return True


def prime_factors(number):
    factors = [1]
    
    i = 1
    while i <= int(math.sqrt(number)):
        if number % i == 0 and is_prime(i):
            factors.append(i)
        i += 2
    
    return factors

'''
What is the largest prime factor of the number 600851475143 ?
'''
def solve(number=600851475143):
    factors = prime_factors(number)
    return factors[len(factors)-1]

class Test(unittest.TestCase):
    def testIsPrime(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        
    def testIsPrimeWithPrimes(self):
        self.assertFalse(is_prime(10, [2,3,5,7]))
        self.assertTrue(is_prime(11, [2,3,5,7]))
        self.assertFalse(is_prime(12, [2,3,5,7,11]))
        
    def testSample(self):
        self.assertEqual(29, solve(13195))
    def testAnswer(self):
        self.assertEqual(6857, solve())
        
        
# -----------------------------------------

def run():
    solve()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    