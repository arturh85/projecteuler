'''
Problem 32
06 December 2002

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
----------------------------------------------------------
Created on 27.01.2015

@author: ahallmann
'''
import unittest
import timeit
import itertools


# an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once like 15234
def is_pandigital(number):
    s = str(number)
    digits = map(int, list(s))
    digits.sort()
    expected = range(1, len(s) + 1)
    return digits == expected

# converts list of integers to number
def to_number(lst):
    if len(lst) == 0:
        return 0
    return int(''.join(map(str, lst)))

def generate_pandigital_numbers(lower=1, upper=9):
    state = range(lower, upper+1)
    for i in itertools.permutations(state):
        n = int(''.join(map(str, list(i))))
        yield n

# checks multiplicand/multiplier/product identity and returns it or None when none found
def find_identity(state):
    for offset in range(2, 5):
        multiplicand = to_number(state[:offset])
        multiplier = to_number(state[offset:5])
        product = to_number(state[5:])
        if multiplicand * multiplier == product:
            return [multiplicand, multiplier, product]
    return None

# 39 x 186 = 7254
# 391867254

class Test(unittest.TestCase):
    def testIsPandigital(self):
        self.assertTrue(is_pandigital(12345))
        self.assertTrue(is_pandigital(51234))
        self.assertFalse(is_pandigital(12344))
        self.assertFalse(is_pandigital(13))
        self.assertFalse(is_pandigital(0))
        self.assertFalse(is_pandigital(2))
        self.assertTrue(is_pandigital(1))

    def testSample(self):
        self.assertEqual([39, 186, 7254], find_identity(list(str(391867254))))
        pass
                             
    def testAnswer(self):
        pass
       
        
# -----------------------------------------

def run():
    products = []
    for i in generate_pandigital_numbers(1, 9):
        identity = find_identity(i)
        if identity:
            print "identity found: " + str(identity[0]) + " * " + str(identity[1]) + ' = ' + str(identity[2])
            products.append(identity[2])

    print "result: " + str(sum(set(products)))

if __name__ == '__main__':
    #run()
    unittest.main()

# if __name__ == '__main__':
#     t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
