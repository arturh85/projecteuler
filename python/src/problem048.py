# coding=utf-8
'''
Problem 48
18 July 2003

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
----------------------------------------------------------
Created on 01.02.2015

@author: ahallmann
'''
import unittest
import timeit

def exp(n):
    return n**n

def solve(n=1000):
    return str(sum(map(exp, range(1, n+1))))[-10:]


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual('0405071317', solve(10))
        pass

    def test_answer(self):
        self.assertEqual('9110846700', solve(1000))
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
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
