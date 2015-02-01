'''
Problem 19
14 June 2002

You are given the following information, but you may prefer to do some research for yourself.

  - 1 Jan 1900 was a Monday.
  - Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

----------------------------------------------------------
Created on 01.02.2012

@author: ahallmann
'''
import unittest
import timeit

def is_leap_year(y):
    if y % 4 == 0: 
        if y % 100 == 0:
            return False
        return True
    return False

_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(month, year):
    days = _days_in_month[month-1]
    
    if month == 2 and is_leap_year(year):
        return days+1
    
    return days
        
def solve():
    cnt = 0
    
    weekday = 0 # monday
    for year in range(1900, 2001):
        for month in range(1, 13):
            for day in range(1, days_in_month(month, year)+1):
                if year > 1900 and day == 1 and weekday == 6: # sunday
                    cnt += 1
                    
                weekday = (weekday + 1) % 7
                
    return cnt

class Test(unittest.TestCase):        
    def testLeapYears(self):
        self.assertEqual(True, is_leap_year(1996))
        self.assertEqual(False, is_leap_year(1997))
        self.assertEqual(False, is_leap_year(2000))
        self.assertEqual(True, is_leap_year(2004))
        
    def testMethods(self):
        self.assertEqual(12, len(_days_in_month))
        self.assertEqual(365, sum(_days_in_month))
                                 
    def testAnswer(self):
        self.assertEqual(171, solve())
        pass
       
        
# -----------------------------------------

def run():
    return solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 10000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    