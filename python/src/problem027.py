'''
Problem 27
27 September 2002

Euler published the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41,
and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n^2 + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number
of primes for consecutive values of n, starting with n = 0.


----------------------------------------------------------
Created on 12.04.2012

@author: ahallmann
'''
import unittest
import timeit
from problem003 import is_prime

def formula(a,b,n):
    return n*n + a*n + b

def find_n(a,b,max_n):
    for n in xrange(0, max_n):
        val = formula(a, b, n)
        prime = is_prime(val)

        if not prime:
            return n-1

    return max_n

def check(a,b,max_n):
    n = find_n(a,b,max_n)
    return n == max_n

def solve(max=1000):
    max_n = 0
    max_n_a = 0
    max_n_b = 0

    for a in range(1, max):
        for b in range(1, max):
            n = find_n(a,b,max)

            if n > max_n:
                max_n = n
                max_n_a = a
                max_n_b = b

            n = find_n(-a,-b,max)

            if n > max_n:
                max_n = n
                max_n_a = -a
                max_n_b = -b

            n = find_n(-a,b,max)

            if n > max_n:
                max_n = n
                max_n_a = -a
                max_n_b = b

            n = find_n(a,-b,max)

            if n > max_n:
                max_n = n
                max_n_a = a
                max_n_b = -b

#    print("max_n: " + str(max_n))
#    print("max_n_a: " + str(max_n_a))
#    print("max_n_b: " + str(max_n_b))

    return max_n_a * max_n_b

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertTrue (check(1, 41, 38))
        self.assertTrue (check(1, 41, 39))
        self.assertTrue (check(1, 41, 40))
        self.assertFalse(check(1, 41, 41))

        self.assertTrue(check(-79, 1601, 79))
        self.assertTrue(check(-79, 1601, 80))
        self.assertFalse(check(-79, 1601, 81))

    def test_answer(self):
        self.assertEquals(-59231, solve())
        pass

        
# -----------------------------------------

def run():
    return solve()
    
if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 100
    print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
