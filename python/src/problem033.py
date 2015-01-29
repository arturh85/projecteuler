'''
Problem 33
20 December 2002

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
----------------------------------------------------------
Created on 29.01.2015

@author: ahallmann
'''
import unittest
import timeit
import itertools


def join_digits(firstDigit, secondDigit):
    return float(str(firstDigit) + str(secondDigit))

def find_curious_fractions():
    numerator_product = 1.0
    denominator_product = 1.0
    for a1 in range(1,10):
        for a2 in range(1,10):
            for b1 in range(1,10):
                for b2 in range(1,10):
                    if a1 == a2 or b1 == b2:
                        continue

                    if a1 == b2:
                        cancel_digit = str(a1)
                    elif a2 == b1:
                        cancel_digit = str(a2)
                    else:
                        continue

                    a = join_digits(a1, a2)
                    b = join_digits(b1, b2)

                    if b <= a:
                        continue

                    c = float(str(a).replace(cancel_digit, ''))
                    d = float(str(b).replace(cancel_digit, ''))

                    if a/b == c/d:
                        print("found curious fraction: " +
                              str(int(a)) + "/" + str(int(b)) + " == " +
                              str(int(c)) + "/" + str(int(d)))
                        numerator_product *= c
                        denominator_product *= d

    print "resulting fraction: " + str(int(numerator_product)) + "/" + str(int(denominator_product))



class Test(unittest.TestCase):
    def testSample(self):
        find_curious_fractions()
        self.assertEqual(49.0/98.0, 4.0/8.0)

    def testAnswer(self):
        pass
       
        
# -----------------------------------------

def run():
    find_curious_fractions()

if __name__ == '__main__':
    run()
    unittest.main()

# if __name__ == '__main__':
#     t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
    
