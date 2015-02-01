'''
Problem 17
17 May 2002

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

----------------------------------------------------------
Created on 30.01.2012

@author: ahallmann
'''
import unittest
import timeit

def digit_to_english(number):
    names = {
        0: "zero",       
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine", 
    }
    
    return names.get(number)


def teens_to_english(number):
    names = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",        
    }
    
    return names.get(number)
    

def twodigit_to_english(number):
    names = {
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    
    return names.get(number)
    

def number_to_english(number):
    if number > 1000: raise Exception("only works with numbers below 1000")
    if number < 0: raise Exception("only works with positive numbers")
    
    if number == 1000: return "one thousend"
    if number < 10: return digit_to_english(number)

    if number < 100:
        if number < 20:
            return teens_to_english(number)
        
        twodigit_number = int(number/10)*10
        twodigit = twodigit_to_english(twodigit_number)
        
        if number % 10 == 0:
            return twodigit
        else:
            return twodigit + "-" + digit_to_english(number % 10)
                
                
    if number % 100 == 0:
        return digit_to_english(int(number/100)) + " hundred"
    else:
        
        return digit_to_english(int(number/100)) + " hundred and " \
            +  number_to_english(number - int(number / 100) * 100)

def custom_str_length(s):
    return len(s) - s.count(" ") - s.count("-")


def solve(limit):
    s = 0
    
    for i in range(1,limit+1):
        s += custom_str_length(number_to_english(i))
        
    return s 


class Test(unittest.TestCase):
    def testInternal(self):
        self.assertEqual("one", digit_to_english(1))
        self.assertEqual("zero", digit_to_english(0))
        self.assertEqual("five", digit_to_english(5))
        
    def testSample(self):
        self.assertEqual("twenty", number_to_english(20))
        self.assertEqual("forty", number_to_english(40))
        self.assertEqual("twenty-one", number_to_english(21))
        self.assertEqual("forty-two", number_to_english(42))

        self.assertEqual("three hundred and forty-two", number_to_english(342))
        self.assertEqual("one hundred and fifteen", number_to_english(115))

        self.assertEqual("nine hundred", number_to_english(900))
        self.assertEqual("nine hundred and ninety-nine", number_to_english(999))
        
        self.assertEqual(23, custom_str_length("three hundred and forty-two"))
        self.assertEqual(20, custom_str_length("one hundred and fifteen"))
        self.assertEqual(19, solve(5))
                                 
    def testAnswer(self):
        self.assertEqual(21124, solve(1000))
        #pass
       
        
# -----------------------------------------

def run():
    return solve(1000)

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    