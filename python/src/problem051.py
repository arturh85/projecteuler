# coding=utf-8
'''
Problem 51
29 August 2003


----------------------------------------------------------
Created on 18.02.2015

@author: ahallmann
'''
import unittest
import timeit
from problem003 import is_prime
from problem003 import generate_primes


def generate_star_variations(s):
    for i in range(10):
        v = s.replace('*', str(i))
        if v[0] == '0':
            continue
        yield v
        
        
def prime_star_variations(s):
    return filter(is_prime, map(int, list(generate_star_variations(s))))


def solve():
    for prime in generate_primes():
        for c in str(prime):
            mask = str(prime).replace(c, '*')
            family = prime_star_variations(mask)
            if len(family) == 8:
                return min(family)
    
    
class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEquals([13, 23, 43, 53, 73, 83], prime_star_variations('*3'))
        self.assertEquals([56003, 56113, 56333, 56443, 56663, 56773, 56993], prime_star_variations('56**3'))

    def test_answer(self):
        self.assertEqual(121313, solve())
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
