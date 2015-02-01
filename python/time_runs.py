'''
Created on 04.02.2012

@author: arturh
'''

import timeit
import math

problems = [
    "Multiples of 3 and 5",
    "Even Fibonacci numbers",
    "Largest prime factor",
    "Largest palindrome product",
    "Smallest multiple",
    "Sum square difference",
    "10001st prime",
    "Largest product in a series",
    "Special Pythagorean triplet",
    "Summation of primes",
    "Largest product in a grid",
    "Highly divisible triangular number",
    "Large sum",
    "Longest Collatz sequence",
    "Lattice paths",
    "Power digit sum",
    "Number letter counts",
    "Maximum path sum I",
    "Counting Sundays",
    "Factorial digit sum",
    "Amicable numbers",
    "Names scores",
    "Non-abundant sums",
    "Lexicographic permutations",
    "1000-digit Fibonacci number",
    "Reciprocal cycles",
    "Quadratic primes",
    "Number spiral diagonals",
    "Distinct powers",
    "Digit fifth powers",
    "Coin sums",
    "Pandigital products",
    "Digit cancelling fractions",
    "Digit factorials",
    "Circular primes",
    "Double-base palindromes",
    "Truncatable primes",
    "Pandigital multiples",
    "Integer right triangles",
    "Champernowne's constant",
    "Pandigital prime",
    "Coded triangle numbers",
    "Sub-string divisibility",
    "Pentagon numbers",
    "Triangular, pentagonal, and hexagonal",
    "Goldbach's other conjecture",
    "Distinct primes factors",
    "Self powers",
    "Prime permutations",
    "Consecutive prime sum"
]


f_tmpl = open("../README.md.tmpl", 'r')
f = open("../README.md", 'w')


line = f_tmpl.readline()
while line:
    f.write(line)
    line = f_tmpl.readline()
f.write("\n")

def makeline(nr, name, result, link1, link2):
    return "| " + str(nr).rjust(4) + " | " + name.rjust(40) + " | " + result.rjust(10) + " | " + link1 + " | " + link2 + " |\n"

# f.write(makeline("#", "Name", "Seconds", "", ""))

for o in range(1, 51):
    t = timeit.Timer("result = run()", "from src.problem%03d" % o + " import run")
    try:
        seconds = t.timeit(1)
        # seconds = 3.3
        result = str(round(seconds, 4)).ljust(6, '0')
    except:
        result = "error"

    link1 = "[Project Euler Problem](https://projecteuler.net/problem=%d)" % o
    link2 = "[Solution Source](https://github.com/arturh85/projecteuler/blob/master/python/src/problem%03d.py)" % o

    line = makeline(o, problems[o-1], result, link1, link2)
    f.write(line)
    print line

f_tmpl.close()
f.close()
