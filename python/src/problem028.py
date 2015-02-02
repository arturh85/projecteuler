'''
Problem 28
11 October 2002

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

----------------------------------------------------------
Created on 12.04.2012

@author: ahallmann
'''
import unittest
import timeit

def print_table(table):
    s = ""
    for row in table:
        for column in row:
            s += str(column) + " "

        s += "\n"

    print(s)


def spiral(size):
    table = [[0 for i in range(size)] for j in range(size)]

    i = 1
    x = (size/2)
    y = (size/2)
    w = 1
    direction = 0

    table[y][x] = i

    for m in range(1, size*size):
        if m != 1 and m % 2 == 1:
            w += 1

        for step in range(1, w+1):
            if direction == 0:
                x += 1
            if direction == 1:
                y += 1
            if direction == 2:
                x -= 1
            if direction == 3:
                y -= 1

            # check if index out of bounds
            if x < 0 or x >= size or y < 0 or y >= size:
                return table

            i += 1
            table[y][x] = i

        direction = (direction + 1) % 4

    return table


def count_diagonal(table, size):
    cnt = 0

    for i in range(0, size):
        cnt += table[i][i]

        if i != size / 2:
            cnt += table[i][size-i-1]

    return cnt



def solve(size=1001):
    table = spiral(size)
    return count_diagonal(table, size)


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEquals(101, solve(5))

    def test_answer(self):
        self.assertEquals(669171001, solve(1001))
        pass

        
# -----------------------------------------

def run():
    return solve()
    
if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 100
    print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
