'''
Created on 04.02.2012

@author: arturh
'''

import timeit
import os

os.chdir("src")

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
    "Consecutive prime sum",
    "Prime digit replacements",
    "Permuted multiples",
    "Combinatoric selections",
    "Poker hands",
    "Lychrel numbers",
    "Powerful digit sum",
    "Square root convergents",
    "Spiral primes",
    "XOR decryption",
    "Prime pair sets",
    "Cyclical figurate numbers",
    "Cubic permutations",
    "Powerful digit counts",
    "Odd period square roots",
    "Convergents of e",
    "Diophantine equation",
    "Maximum path sum II",
    "Magic 5-gon ring",
    "Totient maximum",
    "Totient permutation",
    "Ordered fractions",
    "Counting fractions",
    "Counting fractions in a range",
    "Digit factorial chains",
    "Singular integer right triangles",
    "Counting summations",
    "Prime summations",
    "Coin partitions",
    "Passcode derivation",
    "Square root digital expansion",
    "Path sum: two ways",
    "Path sum: three ways",
    "Path sum: four ways",
    "Monopoly odds",
    "Counting rectangles",
    "Cuboid route",
    "Prime power triples",
    "Product-sum numbers",
    "Roman numerals",
    "Cube digit pairs",
    "Right triangles with integer coordinates",
    "Square digit chains",
    "Arithmetic expressions",
    "Almost equilateral triangles",
    "Amicable chains",
    "Su Doku",
    "Large non-Mersenne prime",
    "Anagramic squares",
    "Largest exponential",
    "Arranged probability"
]


f_tmpl = open("../../README.md.tmpl", 'r')
f = open("../../README.md", 'w')


line = f_tmpl.readline()
while line:
    f.write(line)
    line = f_tmpl.readline()
f.write("\n")

def makeline(nr, name, result, link1, link2):
    return "| " + str(nr).rjust(4) + " | " + name.rjust(40) + " | " + result.rjust(10) + " | " + \
          link1.rjust(60) + " | " + link2.rjust(100) + " |\n"

f.write(makeline("#", "Name", "Seconds", "", ""))
f.write(makeline("-" * 4, "-" * 40, "-" * 10, "-" * 60, "-" * 100))

for o in range(1, 101):
    try:
        t = timeit.Timer("run()", "from src.problem%03d" % o + " import run")
        seconds = t.timeit(1)
        # seconds = 3.3
        result = str(round(seconds, 4)).ljust(6, '0')
        if seconds > 60:
            result = "**" + result + "**"
    except Exception as e:
        print e
        result = ""

    name = problems[o-1]
    link1 = "[Problem](https://projecteuler.net/problem=%d)" % o
    link2 = "[Solution](https://github.com/arturh85/projecteuler/blob/master/python/src/problem%03d.py)" % o
    if not os.path.isfile("problem%03d.py" % o):
        link2 = ""
    line = makeline(o, name, result, link1, link2)
    f.write(line)
    print o, name, result

f_tmpl.close()
f.close()
