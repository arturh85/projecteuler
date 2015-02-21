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
from problem003 import generate_primes
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


cached_primes = primes_between(1, 40000)


def all_concat_prime_with(primes, new_element):
    for prime in primes:
        c = int(str(prime)+str(new_element))
        if c not in cache:
            cache[c] = is_prime(c, cached_primes)
        if not cache[c]:
            return False
        c = int(str(new_element)+str(prime))
        if c not in cache:
            cache[c] = is_prime(c, cached_primes)
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
    
    
def solve(base, ignore_list, limit, target=5):
    for prime in generate_next_consecutive_prime(base, ignore_list, limit):
        consecutive_primes = base + [prime]
        # print "found", consecutive_primes
        if len(consecutive_primes) >= target and sum(consecutive_primes) < limit:
            return consecutive_primes
        next_level = solve(consecutive_primes, ignore_list, limit, target)
        if next_level:
            return next_level
    return None


def generate_next_consecutive_prime(concat_primes, ignore_list, limit=None, debug=False):
    # if not all_concat_prime(concat_primes):
    #     raise Exception('invalid input')
    i = 0
    for prime in cached_primes:
        if debug and i % 10000 == 0:
            print "prime", i, prime
        i += 1
        if prime in ignore_list:
            continue
        if limit and prime > limit:
            return
        if all_concat_prime_with(concat_primes, prime):
            yield prime
    return


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(all_concat_prime([3, 7, 109, 673]))
        self.assertTrue(all_concat_prime([3, 7, 109, 29059]))
        self.assertTrue(all_concat_prime([3, 7, 229]))
        self.assertTrue(all_concat_prime([3, 7, 229, 76819]))
        self.assertTrue(all_concat_prime([3, 7, 541]))
        self.assertTrue(all_concat_prime([3, 7, 541, 4159]))
        self.assertTrue(all_concat_prime([3, 7, 823]))
        self.assertTrue(all_concat_prime([3, 7, 823, 27823]))
        self.assertTrue(all_concat_prime([3, 7, 1237, 471439, 992689]))
        self.assertTrue(all_concat_prime([3, 7, 823, 27823, 3192169]))
        self.assertTrue(all_concat_prime([3, 7, 823, 27823, 3192169]))
        pass
    
    def test_answer(self):
        # self.assertEqual([3, 7, 109], solve([3, 7], [], 3))
        # self.assertEqual([3, 7, 109, 673], solve([3, 7], [], 4))
        
        self.assertEqual(26033, sum([13, 5197, 5701, 6733, 8389]))
        self.assertEqual(34427, sum([7, 1237, 2341, 12409, 18433]))
        self.assertEqual(116501, sum([7, 61, 25939, 26893, 63601]))
        self.assertEqual(231653, sum([7, 19, 8941, 51133, 171553]))
        self.assertEqual(369167, sum([7, 19, 8941, 25867, 334333]))
        self.assertEqual(423841, sum([3, 7, 51133, 96181, 276517]))
        self.assertEqual(446041, sum([3, 7, 19237, 83023, 343771]))
        self.assertEqual(1035037, sum([3, 7, 823, 121441, 912763]))
        self.assertEqual(1252411, sum([3, 7, 2503, 25189, 1224709]))
        self.assertEqual(1465375, sum([3, 7, 1237, 471439, 992689]))
        self.assertEqual(2244919, sum([3, 7, 2707, 471439, 1770763]))
        self.assertEqual(2713957, sum([3, 7, 109, 91159, 2622679]))
        self.assertEqual(2877331, sum([3, 7, 4159, 168331, 2704831]))
        self.assertEqual(2882285, sum([3, 11, 2297, 1353551, 1526423]))
        self.assertEqual(3220825, sum([3, 7, 823, 27823, 3192169]))

        self.assertEqual(26033, sum(solve([], [], 34427, 5)))
        pass


# -----------------------------------------


def run():
    return solve([], [], 34427, 5)


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
