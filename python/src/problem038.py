'''
Problem 38
17 January 2003

Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

----------------------------------------------------------
Created on 29.01.2015

@author: ahallmann
'''
import unittest
import timeit

from problem032 import is_pandigital


def concat_product(n, vector):
    result = ''
    for i in vector:
        result += str(i * n)
    return int(result)


def solve():
    biggest = 0
    for i in range(1, 10000):
        for n in range(2, 7):
            product = concat_product(i, range(1, n))
            if len(str(product)) == 9 and is_pandigital(product):
                # print "found: " + str(product) + " (" + str(i) + " * " + str(range(1, n)) + ")"
                if product > biggest:
                    biggest = product
    # print "solution:" + str(biggest)
    return biggest


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(192384576, concat_product(192, (1, 2, 3)))
        self.assertEqual(918273645, concat_product(9, (1, 2, 3, 4, 5)))
        pass

    def test_answer(self):
        self.assertEqual(932718654, concat_product(9327, (1, 2)))

    pass


# -----------------------------------------

def run():
    return solve()


if __name__ == '__main__':
    run()
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
