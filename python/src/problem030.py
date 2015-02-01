'''
Problem 30
08 November 2002

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
----------------------------------------------------------
Created on 04.10.2012

@author: ahallmann
'''
import unittest
import timeit
import math

def check_number(number, exp):
    if number < 10:
        return False

    i = number
    sum = 0

    while i > 0:
        sum += math.pow(i % 10, exp)

        if sum > number:
            return False

        i /= 10

    return sum == number

def solve():
    s = 0
    for i in range(1, 1000000):
        if check_number(i, 5):
            s += i
    return s

class Test(unittest.TestCase):        
    def test_sample(self):
        self.assertFalse(check_number(1, 4))
        self.assertTrue(check_number(1634, 4))
        self.assertTrue(check_number(8208, 4))
        self.assertTrue(check_number(9474, 4))
        pass
                             
    def test_answer(self):
        pass
       
        
# -----------------------------------------

def run():
    solve()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
