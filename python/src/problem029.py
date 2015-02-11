'''
Problem 29
25 October 2002

Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5:

    2^2=4, 2^3=8, 2^4=16, 2^5=32
    3^2=9, 3^3=27, 3^4=81, 3^5=243
    4^2=16, 4^3=64, 4^4=256, 4^5=1024
    5^2=25, 5^3=125, 5^4=625, 5^5=3125

If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 <= a <= 100 and 2 <= b <= 100?

----------------------------------------------------------
Created on 12.04.2012

@author: ahallmann
'''
import unittest
import timeit
import math

def solve(limit=100):
    values = []

    for a in range(2, limit+1):
        for b in range(2, limit+1):
            values.append(math.pow(a, b))

    return len(set(values))

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEquals(15, solve(5))

    def test_answer(self):
        self.assertEquals(9183, solve(100))
        pass

        
# -----------------------------------------

def run():
    return solve()
    
if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 100
    print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
