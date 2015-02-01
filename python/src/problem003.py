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
import operator

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
            if x > limit:
                return True
            if number % x == 0:
                return False
    return True


def generate_primes():
    discovered = [2]
    yield 2
    i = 3
    while True:
        if is_prime(i, discovered):
            yield i
            discovered.append(i)
        i += 2


def prime_factors(number):
    factors = []
    
    i = 2
    while i <= int(math.sqrt(number))*3:
        if number % i == 0 and is_prime(i):
            factors.append(i)
        i += 2

        if i % 2 == 0:
            i -= 1


    if len(factors) == 0:
        return []

    product = reduce(operator.mul, factors)
    if product < number:
        _f = []
        for factor in factors:
            if factor * product == number:
                _f.append(factor * factor)
            else:
                _f.append(factor)
        return _f
    
    return factors

'''
What is the largest prime factor of the number 600851475143 ?
'''
def solve(number=600851475143):
    return max(prime_factors(number))


class Test(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual([4, 3], prime_factors(12))
        self.assertEqual([2, 7], prime_factors(14))
        self.assertEqual([3, 49], prime_factors(147))
        self.assertEqual([5, 7, 13, 29], prime_factors(13195))

    def test_is_prime(self):
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        
    def test_is_prime_with_primes(self):
        self.assertFalse(is_prime(10, [2,3,5,7]))
        self.assertTrue(is_prime(11, [2,3,5,7]))
        self.assertFalse(is_prime(12, [2,3,5,7,11]))
        
    def test_sample(self):
        self.assertEqual(29, solve(13195))
        pass


    def test_answer(self):
        self.assertEqual(6857, solve(600851475143))
        pass
        
# -----------------------------------------

def run():
    return solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    