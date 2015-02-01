'''
Problem 31
22 November 2002

In England the currency is made up of pound, $, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, $1 (100p) and $2 (200p).
It is possible to make $2 in the following way:

1x$1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can $2 be made using any number of coins?
----------------------------------------------------------
Created on 11.12.2012

@author: ahallmann
'''
import unittest
import timeit

british_coins = [1, 2, 5, 10, 20, 50, 100, 200]


def coinCombinations(val, coins):
    c = sorted(coins, reverse=True)

    # combinations =


def solve():
    pass

# s = 0
# for i in range(1, 1000000):
# if check_number(i, 5):
#         print("found number: " + str(i))
#         s += i
#
# print("sum: " + str(s))


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEquals(200, sum([1 * 100, 1 * 50, 2 * 20, 1 * 5, 1 * 2, 3 * 1]))
        pass

    def test_answer(self):
        pass


# -----------------------------------------

def run():
    raise Exception('not implemented')


if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
