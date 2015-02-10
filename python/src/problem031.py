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


def add_coins(state, coins):
    res = 0
    for i in range(0, len(state)):
        res += state[i] * coins[i]
    return res


def solve(n=200):
    global british_coins
    return solve_recursive(n, british_coins, 0)
    

def solve_recursive(n, coins, i):
    if i == len(coins)-1:
        return 1
    coin = coins[len(coins)-i-1]
    m = 0
    for a in range(n, -1, -coin):
        m += solve_recursive(a, coins, i+1)
    return m
    
    
class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEquals(200, sum([1 * 100, 1 * 50, 2 * 20, 1 * 5, 1 * 2, 3 * 1]))
        self.assertEqual(1, solve(1))
        self.assertEqual(2, solve(2))
        self.assertEqual(2, solve(3))

        pass

    def test_answer(self):
        self.assertEqual(73682, solve(200))
        pass


# -----------------------------------------

def run():
    return solve()

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
