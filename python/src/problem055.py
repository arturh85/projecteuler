# coding=utf-8
'''
Problem 55
24 October 2013

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
----------------------------------------------------------
Created on 19.02.2015

@author: ahallmann
'''
import unittest
import timeit

from problem004 import is_palindrome


def step(n):
    return n + int(str(n)[::-1])


def is_lycherel_number(n):
    for i in range(30):
        n = step(n)
        if is_palindrome(str(n)):
            return False
    return True


def solve():
    cnt = 0
    for n in range(1, 10000):
        if is_lycherel_number(n):
            cnt += 1
    return cnt


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(121, step(47))
        self.assertFalse(is_lycherel_number(47))
        self.assertFalse(is_lycherel_number(349))
        self.assertTrue(is_lycherel_number(196))
        pass
    
    def test_answer(self):
        self.assertEqual(249, solve())
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
