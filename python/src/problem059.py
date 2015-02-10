# coding=utf-8
'''
Problem 59
12 September 2013

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
----------------------------------------------------------
Created on 10.02.2015

@author: ahallmann
'''
import unittest
import collections
import timeit
import string


def encrypt(text, cipher):
    s = []
    
    for i in range(len(text)):
        c = text[i]
        p = cipher[i % len(cipher)]
        
        s.append(str(ord(c) ^ ord(p)))

    return ','.join(s)
    
def decrypt(text, cipher):
    s = text.split(',')
    plaintext = ''
    for i in range(len(s)):
        c = int(s[i])
        p = cipher[i % len(cipher)]
        
        plaintext += chr(c ^ ord(p))
    
    return plaintext
    

def read_cipher(filename):
    f = open(filename, 'r')
    hands = []
    line = f.readline()
    f.close()
    return line

def correct(text):
    permitted = string.ascii_letters + string.whitespace + string.digits + '.!;\',()'
    
    for c in text:
        if c not in permitted:
            return False
    return True
    
    
def char_range(c1, c2):
    for c in xrange(ord(c1), ord(c2)+1):
        yield chr(c)
    
def solve():
    cipher = read_cipher("data/problem059.txt")

    for a in char_range('a', 'z'):
        for b in char_range('a', 'z'):
            for c in char_range('a', 'z'):
                x = decrypt(cipher, a + b + c)
                if correct(x):
                    return sum(map(ord, list(x)))
    return -1

class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual("7,14,14", encrypt("foo", "a"))
        self.assertEqual("foo", decrypt("7,14,14", "a"))
        self.assertTrue(correct("foo"))
        self.assertFalse(correct("föö"))
        self.assertFalse(correct("foo{}"))
        
        pass
    
    def test_answer(self):
        self.assertEqual(107359, solve())
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
