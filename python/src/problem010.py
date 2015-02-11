'''
Problem 10
08 February 2002

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

----------------------------------------------------------
Created on 26.01.2012

@author: ahallmann
'''
import unittest
import timeit
from problem003 import is_prime


def prime_sum(limit):
    if limit < 2: raise ValueError("limit must be >= 2")
    
    primeSum = 2
    primes = [2]
    
    i = 3
    while True:
        if is_prime(i, primes):
            primeSum += i
            primes.append(i)
        i += 2
        
        if i > limit:
            return primeSum

class Test(unittest.TestCase):
    def testFail(self):
        try:
            prime_sum(0)
            self.fail()
        except ValueError:
            pass
            
    def testSampl(self):
        self.assertEqual(17, prime_sum(10))
    def test_answer(self):
        self.assertEqual(142913828922, prime_sum(2000000))
       
        
# -----------------------------------------

def run():
    return prime_sum(2000000)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    