'''
Problem 36
31 January 2003

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
----------------------------------------------------------
Created on 29.01.2015

@author: ahallmann
'''
import unittest
import timeit

from problem004 import is_palindrome

def is_palindrome_base10(number):
    return is_palindrome(str(number))


def is_palindrome_base2(number):
    return is_palindrome(bin(number)[2:])


def solve():
    numbers = []
    for i in range(1, 1000000):
        if is_palindrome_base2(i) and is_palindrome_base10(i):
            numbers.append(i)

    print "result: " + str(sum(numbers))


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(is_palindrome_base2(585))
        self.assertTrue(is_palindrome_base10(585))
        self.assertFalse(is_palindrome_base10(123))
        pass

    def test_answer(self):
        pass


# -----------------------------------------

def run():
    solve()
    pass


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
