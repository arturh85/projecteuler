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


def read_numerals(filename):
    f = open(filename, 'r')
    numerals = []
    for line in f.readlines():
        numerals.append(line.strip())

    f.close()
    return numerals


def format_roman_numeral(number):
    global mapping, order
    sub_numerals = {'I': 10, 'X': 100, 'C': 1000}
    s = ''
    number_index = 0
    while number_index < len(order):
        number_char = order[number_index]
        numeral_value = mapping[number_char]
        for sub_char in sub_numerals:
            sub_value = mapping[sub_char]
            if 1 <= numeral_value - sub_value <= number < numeral_value <= sub_numerals[sub_char]:
                s += sub_char
                number += sub_value
        if number >= numeral_value:
            s += number_char * (number / numeral_value)
            number %= numeral_value
            if number <= 0:
                break
            number_index -= 1
        number_index += 1
    return s
        

def format_roman_numeral_old(number):
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
    global mapping, order

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
    def test_samples(self):

        test_cases = {
            'I': 1,
            'II': 2,
            'IV': 4,
            'XVI': 16,
            'XIX': 19,
            'XLIX': 49,
            'XL': 40,
            'XC': 90,
            'XCV': 95,
            'CD': 400,
            'CM': 900,
            'MMMMDXCV': 4595,
            'MMMMCMXCIX': 4999
        }
        for c in test_cases:
            self.assertEqual(c, format_roman_numeral(test_cases[c]))

    def test_parse_format_compatibility(self):
        for i in range(5000):
            self.assertEqual(i, parse_roman_numeral(format_roman_numeral(i)))
    
    def test_old_new_compatibility(self):
        for i in range(5000):
            self.assertEqual(format_roman_numeral_old(i), format_roman_numeral(i))

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
