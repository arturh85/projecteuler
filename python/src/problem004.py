'''
Problem 4
16 November 2001

A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

----------------------------------------------------------
Created on 25.01.2012

@author: ahallmann
'''
import unittest
import timeit
import itertools
import operator
from multiprocessing import Pool

def is_palindrome(str):
    return str == str[::-1]


'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''


def solve(digits):
    digits_range = range(10 ** (digits - 1), 10 ** digits)
    largest = 0

    for x in digits_range:
        for y in digits_range:
            val = x * y
            if val > largest and is_palindrome(str(val)):
                largest = val

    return largest


def multiply_tuple(t):
    return t[0] * t[1]


def reduce_largest_palindrome(largest, product_tuple):
    product = product_tuple[0] * product_tuple[1]
    if not largest:
        largest = 0
    if product > largest and is_palindrome(str(product)):
        return product
    return largest

def reduce_largest_palindrome2(product_tuple):
    product = product_tuple[0] * product_tuple[1]
    if is_palindrome(str(product)):
        return (product, product)


def solve_functional(digit_count):
    digits_range = range(10 ** (digit_count - 1), 10 ** digit_count)
    products = map(multiply_tuple, itertools.product(digits_range, digits_range))
    palindromes = filter(is_palindrome, map(str, products))
    return max(map(int, palindromes))


def solve_functional_mapreduce(digit_count):
    pool = Pool(processes=8)
    digits_range = range(10 ** (digit_count - 1), 10 ** digit_count)
    products = itertools.product(digits_range, digits_range)
    return pool.map(reduce_largest_palindrome2, products)


    #return reduce(reduce_largest_palindrome, products)


class Test(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(9, solve_functional_mapreduce(1))
        self.assertEqual(9, solve_functional_mapreduce(1))

    def test_sample(self):
        self.assertEqual(9009, solve_functional_mapreduce(2))

    def test_answer(self):
        #self.assertEqual(906609, solve_functional_mapreduce(3))
        pass


# -----------------------------------------

def run():
    solve(3)


if __name__ == '__main__':
# unittest.main()
    pass

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 100
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    