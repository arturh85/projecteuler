'''
Problem 34
03 January 2003

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
----------------------------------------------------------
Created on 29.01.2015

@author: ahallmann
'''
import unittest
import timeit
import math


def is_curious_number(number):
    if number < 10:
        return False

    digits = map(int, list(str(number)))
    return number == sum(map(math.factorial, digits))


def solve():
    curious_numbers = []
    for i in range(1, 100000):
        if is_curious_number(i):
            # print("found curious number: " + str(i))
            curious_numbers.append(i)

    # print "result: " + str(sum(curious_numbers))
    return sum(curious_numbers)


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1, math.factorial(0))
        self.assertEqual(1, math.factorial(1))
        pass

    def test_answer(self):
        self.assertEqual(40730, solve())
        pass


# -----------------------------------------

def run():
    return solve()


if __name__ == '__main__':
    # run()
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
