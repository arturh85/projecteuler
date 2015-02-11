# coding=utf-8
"""
Problem 89
18 February 2005

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way 
of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most 
efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in 
valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for 
this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

----------------------------------------------------------
Created on 10.02.2015

@author: ahallmann
"""
import unittest
import timeit


def read_numerals(filename):
    f = open(filename, 'r')
    numerals = []
    for line in f.readlines():
        numerals.append(line.strip())

    f.close()
    return numerals


def format_roman_numeral(number):
    s = ''
    if 900 <= number < 1000:
        s += 'C'
        number += 100
    while number >= 1000:
        s += 'M'
        number -= 1000
        if 900 <= number < 1000:
            s += 'C'
            number += 100
    if 400 <= number < 500:
        s += 'C'
        number += 100
    if number >= 500:
        s += 'D'
        number -= 500
    if 90 <= number < 100:
        s += 'X'
        number += 10
    while number >= 100:
        s += 'C'
        number -= 100
        if 90 <= number < 100:
            s += 'X'
            number += 10
    if 40 <= number < 50:
        s += 'X'
        number += 10
    if number >= 50:
        s += 'L'
        number -= 50
    if number == 9:
        s += 'I'
        number += 1
    while number >= 10:
        s += 'X'
        number -= 10
        if number == 9:
            s += 'I'
            number += 1
    if number == 4:
        s += 'I'
        number += 1
    if number >= 5:
        s += 'V'
        number -= 5
    while number >= 1:
        s += 'I'
        number -= 1
    return s


def parse_roman_numeral(numeral):
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    order = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    last_order = -1

    s = 0
    for c in numeral:
        if c not in mapping: 
            raise ValueError("unknown char: " + c)

        current_order = order.index(c)
        if current_order < last_order:
            s -= mapping[order[last_order]] * 2
        
        last_order = current_order
        
        s += mapping[c]

    return s


def optimize_roman_numeral(numeral):
    return format_roman_numeral(parse_roman_numeral(numeral))


def solve():
    numerals = read_numerals("data/problem089.txt")
    savings = 0
    for numeral in numerals:
        o = optimize_roman_numeral(numeral)
        savings += len(numeral) - len(o)
    return savings


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(16, parse_roman_numeral('XVI'))
        self.assertEqual('XVI', format_roman_numeral(16))
        self.assertEqual(4, parse_roman_numeral('IV'))
        self.assertEqual('IV', format_roman_numeral(4))
        self.assertEqual(19, parse_roman_numeral('XIX'))
        self.assertEqual('XIX', format_roman_numeral(19))
        self.assertEqual(40, parse_roman_numeral('XL'))
        self.assertEqual('XL', format_roman_numeral(40))
        self.assertEqual(90, parse_roman_numeral('XC'))
        self.assertEqual('XC', format_roman_numeral(90))
        self.assertEqual(400, parse_roman_numeral('CD'))
        self.assertEqual('CD', format_roman_numeral(400))
        self.assertEqual(900, parse_roman_numeral('CM'))
        self.assertEqual('CM', format_roman_numeral(900))
        self.assertEqual('MMMMDXCV', format_roman_numeral(4595))
        self.assertEqual('XCV', format_roman_numeral(95))
        
        for i in range(10000):
            self.assertEqual(i, parse_roman_numeral(format_roman_numeral(i)))
        pass
    
    def test_answer(self):
        self.assertEqual(743, solve())
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
