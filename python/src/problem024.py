'''
Problem 24
16 August 2002

A permutation is an ordered arrangement of objects. For example, 3124 
is one possible permutation of the digits 1, 2, 3 and 4. If all of the 
permutations are listed numerically or alphabetically, we call it lexicographic 
order. 

The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation 
of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

----------------------------------------------------------
Created on 04.02.2012

@author: ahallmann
'''
import unittest
import timeit
import math

lexicographic_permutations_cache = {}

def lexicographic_permutations(objects):
    if lexicographic_permutations_cache.has_key(objects):
        for x in lexicographic_permutations_cache[objects]:
            yield x
    
    cnt = len(objects)
    if cnt == 1: yield objects
    
    for first in objects:
        rest = objects.replace(first, '')
        cache_value = ''
        for others in lexicographic_permutations(rest):
            cache_value += others
            yield first + others
        
        #lexicographic_permutations_cache[rest] = cache_value
            
        
 
def solve(objects='0123456789', index=1000000):
    i = 1
    for x in lexicographic_permutations(objects):
        if i == index:
            return x
        i += 1
        
 
class Test(unittest.TestCase):        
    def test_sample(self):
        # n! = number of permutations
        self.assertEquals(2, math.factorial(len('01')))
        self.assertEquals(6, math.factorial(len('012')))
        
        self.assertEquals(['01', '10'], list(lexicographic_permutations('01')))

        
        self.assertEquals(['012', '021', '102', '120', '201', '210'], list(lexicographic_permutations('012')))
                             
    def testAnswer(self):
        self.assertEquals('2783915460', solve())
       
        
# -----------------------------------------

def run():
    return solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 1
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    