'''
Problem 16
03 May 2002

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

----------------------------------------------------------
Created on 30.01.2012

@author: ahallmann
'''
import unittest
import timeit

def digit_sum(number):
    digit_sum = 0
    for c in str(number):
        digit_sum += int(c)
        
    return digit_sum

class Test(unittest.TestCase):
    def testSample(self):
        self.assertEqual(26, digit_sum(2**15))
    def testAnswer(self):
        self.assertEqual(1366, digit_sum(2**1000))
       
        
# -----------------------------------------

def run():
    return digit_sum(2**1000)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    