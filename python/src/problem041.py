'''
Problem 40
28 March 2003

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

----------------------------------------------------------
Created on 30.01.2015

@author: ahallmann
'''
import unittest
import timeit

from problem003 import generate_primes
from problem032 import is_pandigital

def solve():
    largest = 0
    for prime in generate_primes():
        if is_pandigital(prime):
            largest = prime
            
        if prime > 10000000:
            return largest
                  

class Test(unittest.TestCase):
    def test_sample(self):
        pass

    def test_answer(self):
        self.assertEqual(7652413, solve())
        pass



# -----------------------------------------

def run():
    return solve()


if __name__ == '__main__':
    run()
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
