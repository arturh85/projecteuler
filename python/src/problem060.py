# coding=utf-8
"""
Problem 60
12 September 2013

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them
 in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are 
 prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with 
 this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
----------------------------------------------------------
Created on 10.02.2015

@author: ahallmann
"""
import unittest
import timeit
import string
import itertools


from problem003 import is_prime
from problem049 import primes_between


cache = {}

def all_concat_prime(p):
    for combination in itertools.permutations(p, 2):
        c = int(str(combination[0])+str(combination[1]))
        if c not in cache:
            cache[c] = is_prime(c)
        if not cache[c]:
            return False
    return True   

    
    
def prime_combinations(primes, n=2):
    if n == 1:
        for prime in primes:
            yield [prime]
        return
    
    for i in primes:
        for m in prime_combinations(primes, n-1):
            if i in m:
                continue
            yield m + [i]
    
    
def solve(n=5, limit=1000):
    primes = list(primes_between(1, limit))
    for l in prime_combinations(primes, n):
        if all_concat_prime(l):
            return sum(l)
    return None


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(all_concat_prime([3, 7, 109, 673]))
        self.assertEqual(792, solve(4))
        pass
    
    def test_answer(self):
        self.assertEqual(792, solve())
        pass


# -----------------------------------------


def run():
    return solve()


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
