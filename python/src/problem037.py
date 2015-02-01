'''
Problem 37
17 January 2003

The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
----------------------------------------------------------
Created on 29.01.2015

@author: ahallmann
'''
import unittest
import timeit

from problem003 import generate_primes
from problem003 import is_prime


def is_truncatable_prime(prime):
    if prime < 10:
        return False

    digits = str(prime)
    while len(digits) > 1:
        digits = digits[1:]
        if not is_prime(int(digits)):
            return False

    digits = str(prime)
    while len(digits) > 1:
        digits = digits[:-1]
        if not is_prime(int(digits)):
            return False

    return True


def solve():
    numbers = []
    for prime in generate_primes():
        if is_truncatable_prime(prime):
            numbers.append(prime)
            if len(numbers) >= 11:
                break
    return sum(numbers)


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(is_truncatable_prime(3797))
        self.assertFalse(is_truncatable_prime(61))

    def test_answer(self):
        pass


# -----------------------------------------

def run():
    solve()
    pass


if __name__ == '__main__':
    run()
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
