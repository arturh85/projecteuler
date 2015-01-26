'''
Problem 23
02 August 2002

A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 
28123 can be written as the sum of two abundant numbers. However, this upper 
limit cannot be reduced any further by analysis even though it is known that 
the greatest number that cannot be expressed as the sum of two abundant 
numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.

----------------------------------------------------------
Created on 04.02.2012

@author: ahallmann
'''
import unittest
import timeit

from problem021 import proper_divisors


def solve(limit=28123):
    abundant_numbers = []
    _sum = 0
    
    for x in range(1, limit):
        d = deficient_perfect_or_abundant(x)
        if d > 0:
            abundant_numbers.append(x)
                    
    for x in range(1, limit):
        sum_of_two_abundant_numbers = True
        for a in abundant_numbers:
            m = x - a
            if m < 0: break
            
            if deficient_perfect_or_abundant(m) > 0:
                sum_of_two_abundant_numbers = False
                break
                
        if sum_of_two_abundant_numbers == True:
            _sum += x
            
    return _sum


'''
returns the type of number:

sum-n < 0 = deficient
sum-n = 0 = perfect
sum-n > 0 = abundant    
'''

deficient_perfect_or_abundant_cache = {}


def deficient_perfect_or_abundant(n):
    if deficient_perfect_or_abundant_cache.has_key(n):
        return deficient_perfect_or_abundant_cache[n]
    
    k = sum(proper_divisors(n)) - n
    deficient_perfect_or_abundant_cache[n] = k
    return k        

class Test(unittest.TestCase):        
    def testSample(self):
        self.assertEqual(28, sum(proper_divisors(28)))
        self.assertEquals(0, deficient_perfect_or_abundant(28))
        self.assertLess(0, deficient_perfect_or_abundant(12))
                             
    def testAnswer(self):
        self.assertEqual(4179871, solve())
       
        
# -----------------------------------------

def run():
    solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    