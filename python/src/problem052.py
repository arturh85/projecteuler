# coding=utf-8
'''
Problem 52
12 September 2013

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
----------------------------------------------------------
Created on 01.02.2015

@author: ahallmann
'''
import unittest
import timeit

from problem049 import primes_between

def generate_numbers(start=1):
	i = start
	while True:
		yield i
		i += 1
		
def same_digits(a, b):
	a = str(a)
	b = str(b)
	
	if len(a) != len(b):
		return False
		
	for c in list(a):
		if c not in b:
			return False
		
	return True
		
	
def have_same_digits(numbers):
	if len(numbers) == 0:
		return True
	first = numbers[0]
	for i in range(1, len(numbers)):
		if not same_digits(first, numbers[i]):
			return False
	return True


def solve():
	for num in generate_numbers():
		canary = num*6
		if not same_digits(num, canary):
			continue
		
		numbers = [num, num*2, num*3, num*4, num*5, canary]
		
		if have_same_digits(numbers):
			print numbers
			return num
	
class Test(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(have_same_digits([123, 321]))
        self.assertFalse(have_same_digits([123, 323]))
        self.assertTrue(have_same_digits([125874, 2*125874]))
        pass

    def test_answer(self):
        self.assertEqual(142857, solve())
        pass

# -----------------------------------------


def run():
    return solve()
    pass


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
