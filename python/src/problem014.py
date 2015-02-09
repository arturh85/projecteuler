'''
Problem 14
05 April 2002

The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3*n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) 
contains 10 terms. Although it has not been proved yet (Collatz Problem), 
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

----------------------------------------------------------


Created on 29.01.2012

@author: ahallmann
'''
import unittest
import timeit


def sequence(start):
    i = start
    while i != 1:
        yield i
        i = sequence_next(i)
    yield i


def sequence_next(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1


def sequence_list(start):
    lst = []
    for i in sequence(start):
        lst.append(i)

    return lst


sequence_length_cache = {}


def sequence_length(i):   
    global sequence_length_cache
    if i == 1:
        return 1
    
    if i in sequence_length_cache:
        return sequence_length_cache[i]

    subsequence_length = 1 + sequence_length(sequence_next(i))
    sequence_length_cache[i] = subsequence_length
    return subsequence_length


def solve(limit=1000000):
    longest_cnt = 0
    longest_start = 0
    
    for i in xrange(1, limit):
        cnt = sequence_length(i)
        
        if cnt > longest_cnt:
            longest_cnt = cnt
            longest_start = i
            
    return longest_start


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual([13, 40, 20, 10, 5, 16, 8, 4, 2, 1], sequence_list(13))
            
    def test_answer(self):
        self.assertEqual(837799, solve())
       
        
# -----------------------------------------

def run():
    return solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
