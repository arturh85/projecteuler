# coding=utf-8
'''
Problem 54
12 September 2013

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, 
a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both 
players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if 
the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:
...[table]...

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): the first five are 
Player 1's cards and the last five are Player 2's cards. You can assume that all hands 
are valid (no invalid characters or repeated cards), each player's hand is in no specific order, 
and in each hand there is a clear winner.

How many hands does Player 1 win?

----------------------------------------------------------
Created on 01.02.2015

@author: ahallmann
'''
import unittest
import timeit



def read_hands(filename):
	f = open(filename, 'r')
	hands = []
	for line in f.readlines():
		cards = line.strip().split(" ")
		hands.append([cards[0:5], cards[5:]])

	f.close()
	return hands

	
def first_char(str):
	return str[0]
	
	
def score_hand(hand):
	card_values = map(first_char, hand)
	return 0
	
	
def player1_wins(hands):
	return score_hand(hands[0]) > score_hand(hands[1])
	
def solve():
	return len(filter(player1_wins, read_hands("data/problem054.txt")))
	
class Test(unittest.TestCase):
	def test_sample(self):
		pass

	def test_answer(self):
		pass

# -----------------------------------------


def run():
	raise Exception("not implemented")
	pass


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
# t = timeit.Timer("run()", "from __main__ import run")
# count = 1
# print(str(t.timeit(count)) + " seconds for " + str(count) + " runs")
