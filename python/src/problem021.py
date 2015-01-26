'''
Problem 21
05 July 2002

Let d(n) be defined as the sum of proper divisors of n (numbers less 
than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable 
pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 
2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

----------------------------------------------------------
Created on 04.02.2012

@author: ahallmann
'''
import unittest
import timeit

def proper_divisors(n):
    for x in range(1, int(n/2)+1):
        if n % x == 0:
            yield x

def d(n):
    return sum(proper_divisors(n))

def solve(limit):
    amicable_numbers = []
    
    for a in range(1,limit):
        b = d(a)
                
        if a != b and d(b) == a: 
            amicable_numbers.append(a)

    return amicable_numbers

class Test(unittest.TestCase):        
    def testSample(self):
        self.assertEqual(284, d(220))
        self.assertEqual(220, d(284))
                                 
    def testAnswer(self):
        amicable_numbers = solve(10000)
        
        self.assertEqual(\
             [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368], \
             amicable_numbers)
        
        self.assertEqual(31626, sum(amicable_numbers))
    pass
       
        
# -----------------------------------------

def run():
    solve(10000)

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    