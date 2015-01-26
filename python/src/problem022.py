'''
Problem 22
19 July 2002

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into 
alphabetical order. Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain 
a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

----------------------------------------------------------
Created on 04.02.2012

@author: ahallmann
'''
import unittest
import timeit

def read_names(filename):
    f = open(filename, 'r')
    names = f.readline().replace('"', '').split(',')
    f.close()
    return names

names = read_names('data/problem022.txt')
names.sort()

def solve():
    scores = 0
    i = 1
    for name in names:
        scores += score(name, i)
        i += 1

    return scores

def score(name, position):
    score = 0
    for c in name:
        score += ord(c)-ord('A') + 1

    return score * position
 
class Test(unittest.TestCase):        
    def testSample(self):
        self.assertEqual(49714, score('COLIN', 938))
                             
    def testAnswer(self):
        self.assertEqual(871198282, solve())       
        
# -----------------------------------------

def run():
    solve()

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    t = timeit.Timer("run()", "from __main__ import run")
    count = 100000
    print str(t.timeit(count)) + " seconds for " + str(count) + " runs"
    
    