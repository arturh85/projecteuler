'''
Problem 42
25 April 2003

The nth term of the sequence of triangle numbers is given by, tn = 1/2 n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a
triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
----------------------------------------------------------
Created on 30.01.2015

@author: ahallmann
'''
import unittest
import timeit


def triangle_numbers_at(n):
    return 1.0 / 2.0 * n * (n + 1)


def generate_numbers(func):
    i = 1
    while True:
        value = func(i)
        yield value
        i += 1


def generate_triangle_numbers():
    return generate_numbers(triangle_numbers_at)

is_number_cache = {}


def is_number(func, cache_name, n):
    global is_number_cache

    if cache_name not in is_number_cache:
        is_number_cache[cache_name] = {
            "max": 0,
            "list": []
        }

    if is_number_cache[cache_name]["max"] < n:
        while True:
            is_number_cache[cache_name]["max"] += 1
            value = func(is_number_cache[cache_name]["max"])
            is_number_cache[cache_name]["list"].append(value)
            if value > n:
                break

    return n in is_number_cache[cache_name]["list"]


def is_triangle_number(n):
    return is_number(triangle_numbers_at, 'triangle', n)


def char_value(char):
    return ord(char) - ord('A') + 1


def word_value(word):
    return sum(map(char_value, list(word)))


def read_words(filename):
    f = open(filename, 'r')
    words = []
    for line in f.readlines():
        words = line[1:-1].split('","')

    f.close()
    return words


def solve():
    words = read_words("data/problem042.txt")
    word_values = map(word_value, words)
    triangle_numbers = filter(is_triangle_number, word_values)
    return len(triangle_numbers)


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(1.0, triangle_numbers_at(1.0))
        self.assertEqual(3.0, triangle_numbers_at(2.0))
        self.assertEqual(6.0, triangle_numbers_at(3.0))

        self.assertEqual(55, word_value('SKY'))

        self.assertEqual(19, char_value('S'))
        self.assertEqual(11, char_value('K'))
        self.assertEqual(25, char_value('Y'))
        pass

    def test_answer(self):
        self.assertEqual(162, solve())
        pass


# -----------------------------------------

def run():
    solve()
    pass


if __name__ == '__main__':
    run()
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
#     count = 1
#     print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
