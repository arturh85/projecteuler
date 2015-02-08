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
import collections
import timeit



card_values_map = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

card_suites_map = {
    'H': 0,
    'C': 1,
    'D': 2,
    'S': 3
}


def card_value(card):
    global card_values_map
    return card_values_map.get(card[0])


def card_suite(card):
    global card_suites_map
    return card_suites_map.get(card[1])


def read_hands(filename):
    f = open(filename, 'r')
    hands = []
    for line in f.readlines():
        cards = line.strip().split(" ")
        hands.append([cards[0:5], cards[5:]])

    f.close()
    return hands


def first_char(s):
    return s[0]


def _score_royal_flush(hand):
    card_values = map(card_value, hand)
    if max(card_values) != 14:
        return 0
        
    straight_flush_score = _score_straight_flush(hand)
    
    if straight_flush_score == 0:
        return 0
    
    return 2000 + straight_flush_score


def _score_straight_flush(hand):
    suites = set(map(card_suite, hand))
    if len(suites) != 1:
        return 0
    
    straight_score = _score_straight(hand)
    if straight_score == 0:
        return 0
    
    return 2000 + straight_score


def _score_four_of_a_kind(hand):
    card_values = map(card_value, hand)
    four_of_a_kinds = [x for x, y in collections.Counter(card_values).items() if y == 4]
    if len(four_of_a_kinds) != 1:
        return 0
    others = [x for x, y in collections.Counter(card_values).items() if y == 1]
    
    return 3000 + 10 * four_of_a_kinds[0] + others[0]


def _score_full_house(hand):
    card_values = map(card_value, hand)
    pairs = [x for x, y in collections.Counter(card_values).items() if y == 2]
    if len(pairs) != 1:
        return 0
    three_of_a_kinds = [x for x, y in collections.Counter(card_values).items() if y == 3]
    if len(three_of_a_kinds) != 1:
        return 0

    return 1400 + 100 * three_of_a_kinds[0] + 10 * pairs[0]


def _score_flush(hand):
    card_values = map(card_value, hand)
    suites = set(map(card_suite, hand))
    if len(suites) != 1:
        return 0
    return 1300 + sum(card_values)


def _score_straight(hand):
    card_values = map(card_value, hand)
    card_values.sort()
    for i in range(len(card_values) - 1):
        if card_values[i] + 1 != card_values[i + 1]:
            return 0
    return 1200 + sum(card_values)


def _score_three_of_a_kind(hand):
    card_values = map(card_value, hand)
    pairs = [x for x, y in collections.Counter(card_values).items() if y == 3]
    if len(pairs) != 1:
        return 0
    others = [x for x, y in collections.Counter(card_values).items() if y == 1]

    return 700 + 30 * pairs[0] + sum(others)


def _score_two_pairs(hand):
    card_values = map(card_value, hand)
    pairs = [x for x, y in collections.Counter(card_values).items() if y == 2]
    if len(pairs) != 2:
        return 0

    others = [x for x, y in collections.Counter(card_values).items() if y == 1]
    return 200 + 20 * pairs[0] + 20 * pairs[1] + sum(others)


def _score_one_pair(hand):
    card_values = map(card_value, hand)
    pairs = [x for x, y in collections.Counter(card_values).items() if y == 2]
    if len(pairs) != 1:
        return 0

    others = [x for x, y in collections.Counter(card_values).items() if y == 1]
    return 60 + 10 * pairs[0] + sum(others)
        

def _score_high_card(hand):
    card_values = map(card_value, hand)
    return 2 * max(card_values) + sum(card_values)


def score_hand(hand):
    score = _score_royal_flush(hand)
    if score > 0: 
        return score
    score = _score_straight_flush(hand)
    if score > 0:
        return score
    score = _score_four_of_a_kind(hand)
    if score > 0:
        return score
    score = _score_full_house(hand)
    if score > 0:
        return score
    score = _score_flush(hand)
    if score > 0:
        return score
    score = _score_straight(hand)
    if score > 0:
        return score
    score = _score_three_of_a_kind(hand)
    if score > 0:
        return score
    score = _score_two_pairs(hand)
    if score > 0:
        return score
    score = _score_one_pair(hand)
    if score > 0:
        return score
    return _score_high_card(hand)


def player1_wins(hands):
    score1 = score_hand(hands[0])
    score2 = score_hand(hands[1])
    
    if score1 == score2:
        print hands, score1, score2

    return score1 > score2


def solve():
    hands = read_hands("data/problem054.txt")
    relevant_hands = filter(player1_wins, hands)
    return len(relevant_hands)


def parse(s):
    return s.split(" ")


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(14, card_value('AD'))
        self.assertEqual(75, score_hand(['5D', '8C', '9S', 'JS', 'AC']))
        self.assertEqual(136, score_hand(['5H', '5C', '6S', '7S', 'KD']))
        
        self.assertFalse(player1_wins([parse('5H 5C 6S 7S KD'), parse('2C 3S 8S 8D TD')]))
        self.assertTrue(player1_wins([parse('5D 8C 9S JS AC'), parse('2C 5C 7D 8S QH')]))
        self.assertFalse(player1_wins([parse('2D 9C AS AH AC'), parse('3D 6D 7D TD QD')]))
        self.assertTrue(player1_wins([parse('4D 6S 9H QH QC'), parse('3D 6D 7H QD QS')]))
        self.assertTrue(player1_wins([parse('2H 2D 4C 4D 4S'), parse('3C 3D 3S 9S 9D')]))
        pass
    
    def test_limits(self):
        self.assertEqual(35, score_hand(['2D', '3C', '4S', '5S', '7C'])) # worst high card possible
        self.assertEqual(87, score_hand(['9D', 'JC', 'QS', 'KS', 'AC'])) # best high card possible
        self.assertEqual(92, score_hand(['2D', '2C', '3S', '4S', '5C'])) # worst one-pair possible
        self.assertEqual(236, score_hand(['AD', 'AC', 'KS', 'QS', 'JC'])) # best one-pair possible
        self.assertEqual(304, score_hand(['2D', '2C', '3S', '3S', '4C'])) # worst two-pair possible
        self.assertEqual(752, score_hand(['AD', 'AC', 'KS', 'KS', 'QC'])) # best two-pair possible
        self.assertEqual(767, score_hand(['2D', '2C', '2S', '3S', '4D'])) # worst three of a kind possible
        self.assertEqual(1145, score_hand(['AD', 'AC', 'AS', 'KS', 'QD'])) # best three of a kind possible
        self.assertEqual(1220, score_hand(['2D', '3C', '4S', '5S', '6D'])) # worst straight possible
        self.assertEqual(1260, score_hand(['AD', 'KC', 'QS', 'JD', 'TD'])) # best straight possible
        self.assertEqual(1321, score_hand(['2D', '3D', '4D', '5D', '7D'])) # worst flush possible
        self.assertEqual(1359, score_hand(['AS', 'KS', 'QS', 'JS', '9S'])) # best flush possible
        self.assertEqual(1630, score_hand(['2D', '2S', '2C', '3S', '3D'])) # worst full house possible
        self.assertEqual(2930, score_hand(['AD', 'AS', 'AC', 'KS', 'KD'])) # best full house possible
        self.assertEqual(3023, score_hand(['2D', '2S', '2C', '2S', '3D'])) # worst four of a kind possible
        self.assertEqual(3153, score_hand(['AD', 'AS', 'AC', 'AS', 'KD'])) # best four of a kind possible
        self.assertEqual(3220, score_hand(['2D', '3D', '4D', '5D', '6D'])) # worst straight-flush possible
        self.assertEqual(3255, score_hand(['KD', 'QD', 'JD', 'TD', '9D'])) # best straight-flush possible
        self.assertEqual(5260, score_hand(['AD', 'KD', 'QD', 'JD', 'TD'])) # royal flush
        pass

    def test_answer(self):
        self.assertEqual(389, solve())
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
