# coding=utf-8
'''
Problem 39
14 March 2003

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
----------------------------------------------------------
Created on 02.02.2015

@author: ahallmann
'''
import unittest
import timeit
import math


def find_solutions(p):
    solutions = []
    for a in range(1, p/4+1):
        for b in range(a+1, (p-a)/2):
            if a + b >= p:
                continue
            c = math.sqrt(a*a + b*b)
            s = {a, b, int(c)}
            if a + b + c == p and s not in solutions:
                solutions.append(s)
                
    return solutions


def solve():
    max_solutions_number = 0
    max_solutions = 0
    for i in range(1, 1000):
        solutions = find_solutions(i)
        if len(solutions) > max_solutions:
            max_solutions = len(solutions)
            max_solutions_number = i
    return max_solutions_number


class Test(unittest.TestCase):
    def test_sample(self):
        a = {20, 48, 52}
        b = {24, 45, 51}
        c = {30, 40, 50}
        self.assertEqual(120, sum(a))
        self.assertEqual(120, sum(b))
        self.assertEqual(120, sum(c))
        self.assertEqual([a, b, c], find_solutions(120))

    def test_answer(self):
        self.assertEqual(840, solve())
        pass


def run():
    return solve()


if __name__ == '__main__':
    run()
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
