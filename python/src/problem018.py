'''
Problem 18
31 May 2002

By starting at the top of the triangle below and moving to adjacent
 numbers on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve 
this problem by trying every route. However, Problem 67, is the 
same challenge with a triangle containing one-hundred rows; it 
cannot be solved by brute force, and requires a clever method! ;o)

----------------------------------------------------------
Created on 31.01.2012

@author: ahallmann
'''
import unittest
import timeit
import sys

subroute_lookup_table = {}



HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def max_sum_route(triangle, lookahead, print_route=False):
    subroute_lookup_table.clear()
    lookahead = max(1, lookahead)
    i = 0
    pathsum = 0
    
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

        pathsum += value
                
        if line < len(triangle)-1:
            path1 = max_sum_subroute(triangle, i, line+1, \
                                     min(line+lookahead, len(triangle)-1))
            path2 = max_sum_subroute(triangle, i+1, line+1, \
                                     min(line+lookahead, len(triangle)-1))
            
            
            if path2 > path1:
                i += 1
        
    return pathsum
    
def max_sum_subroute(triangle, i, startline, endline):
    lookup_index = startline * 100000 + i + endline * 1000
    if subroute_lookup_table.has_key(lookup_index):
        return subroute_lookup_table.get(lookup_index)
    
    pathsum = triangle[startline][i]
    if startline != endline:
        path1 = max_sum_subroute(triangle, i, startline+1, endline)
        path2 = max_sum_subroute(triangle, i+1, startline+1, endline)
        
        if path1 > path2:
            pathsum += path1
        else:
            pathsum += path2
        
    subroute_lookup_table[lookup_index] = pathsum
    
    return pathsum    


triangle_1 = [
       [3],
      [7, 4],
     [2, 4, 6],
    [8, 5, 9, 3],
]

triangle_2 = [
                                [75],
                              [95, 64],
                            [17, 47, 82],
                          [18, 35, 87, 10],
                        [20, 4, 82, 47, 65],
                      [19, 1, 23, 75, 3, 34],
                    [88, 2, 77, 73, 7, 63, 67],
                  [99, 65, 4, 28, 6, 16, 70, 92],
                [41, 41, 26, 56, 83, 40, 80, 70, 33],
              [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
          [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
      [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]              
]

triangle_3 = [
                                [1],
                              [11, 1],
                            [11, 1, 1],
                          [11, 1, 1, 1],
                        [11, 1, 1, 1, 1],
                      [11, 1, 1, 1, 1, 11111111],               
]

class Test(unittest.TestCase):        
    def testSample(self):
        self.assertEqual(23, max_sum_route(triangle_1, 1))
        self.assertEqual(23, max_sum_route(triangle_1, 2))
        
    def testLookahead(self):
        self.assertEqual(56, max_sum_route(triangle_3, 1))
        self.assertEqual(56, max_sum_route(triangle_3, 2))
        self.assertEqual(56, max_sum_route(triangle_3, 3))
        self.assertEqual(56, max_sum_route(triangle_3, 4))
        self.assertEqual(11111116, max_sum_route(triangle_3, 5))

                                 
    def testAnswer(self):
        self.assertEqual(1064, max_sum_route(triangle_2, 1))
        self.assertEqual(1074, max_sum_route(triangle_2, 2))
        self.assertEqual(1074, max_sum_route(triangle_2, 3))
        self.assertEqual(1074, max_sum_route(triangle_2, 15))
        
    def test_print(self):
        self.assertEqual(1074, max_sum_route(triangle_2, 3, True))

        
# -----------------------------------------

def run():
    return max_sum_route(triangle_2, 2)

if __name__ == '__main__':
    # unittest.main()
    max_sum_route(triangle_2, 2, True)

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    