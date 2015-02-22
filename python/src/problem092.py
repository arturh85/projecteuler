# coding=utf-8
"""
Problem 92
01 April 2005

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
----------------------------------------------------------
Created on 22.02.2015

@author: ahallmann
"""
import unittest
import timeit
import sys

def chain_next(n):
    a = 0
    while n > 0:
        a += (n % 10) ** 2
        n /= 10
    return a

cache = {}


def chain(n):
    if n in cache:
        return cache[n]
    m = chain_next(n)
    if m == 1:
        cache[n] = 1
        return 1
    if m == 89:
        cache[n] = 89
        return 89
    return chain(m)
    

def solve():
    n = 0
    for i in range(1, 10000000):
        if chain(i) == 89:
            n += 1
    return n


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(32, chain_next(44))
        self.assertEqual(1, chain(44))
        self.assertEqual(89, chain(85))
        pass
    
    def test_answer(self):
        self.assertEqual(8581146, solve())
        pass


# -----------------------------------------


def run():
    return solve()


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
