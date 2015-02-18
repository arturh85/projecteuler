# coding=utf-8
"""
Problem 81
22 October 2004

In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by only moving to the right and down, is indicated in bold red and is equal to 2427.



Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 
80 by 80 matrix, from the top left to the bottom right by only moving right and down.
----------------------------------------------------------
Created on 16.02.2015

@author: ahallmann
"""
import unittest
import timeit
import sys

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


matrix1 = [
    [131, 673, 234, 103,  18],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524,  37, 331]
]

subroute_lookup_table = {}


def read_matrix(filename):
    f = open(filename, 'r')
    numerals = []
    for line in f.readlines():
        numerals.append(line.strip())

    f.close()
    return numerals


def min_sum_route(triangle, lookahead, print_route=False):
    subroute_lookup_table.clear()
    lookahead = max(1, lookahead)
    i = 0
    path_sum = 0

    bottom_row_length = len(triangle[len(triangle) - 1])
    for line in range(0, len(triangle)):
        value = triangle[line][i]
        if print_route:
            for k in range(bottom_row_length/2 - line/2):
                sys.stdout.write("  ")
            for j in range(0, len(triangle[line])):
                c = str(triangle[line][j])
                if j == i:
                    c = FAIL + str(c) + ENDC
                sys.stdout.write(c + " ")
            sys.stdout.write("\n")

        path_sum += value

        if line < len(triangle)-1:
            path1 = min_sum_subroute(triangle, i, line+1, \
                                     min(line+lookahead, len(triangle)-1))
            path2 = min_sum_subroute(triangle, i+1, line+1, \
                                     min(line+lookahead, len(triangle)-1))


            if path2 < path1:
                i += 1

    return path_sum


def min_sum_subroute(triangle, i, start_line, end_line):
    lookup_index = start_line * 100000 + i + end_line * 1000
    if subroute_lookup_table.has_key(lookup_index):
        return subroute_lookup_table.get(lookup_index)
    path_sum = triangle[start_line][i]
    if start_line != end_line:
        path1 = min_sum_subroute(triangle, i, start_line+1, end_line)
        path2 = min_sum_subroute(triangle, i+1, start_line+1, end_line)

        if path1 > path2:
            path_sum += path1
        else:
            path_sum += path2

    subroute_lookup_table[lookup_index] = path_sum

    return path_sum

def solve():
    pass


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual()
        pass
    
    def test_answer(self):
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
