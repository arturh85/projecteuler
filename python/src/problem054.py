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
    
    return 1000000 + straight_flush_score


def _score_straight_flush(hand):
    suites = set(map(card_suite, hand))
    if len(suites) != 1:
        return 0
    
    straight_score = _score_straight(hand)
    if straight_score == 0:
        return 0
    
    return 2600000 + straight_score


def _score_four_of_a_kind(hand):
    card_values = map(card_value, hand)
    four_of_a_kinds = [x for x, y in collections.Counter(card_values).items() if y == 4]
    if len(four_of_a_kinds) != 1:
        return 0
    others = [x for x, y in collections.Counter(card_values).items() if y == 1]
    
    return 1100000 + 100000 * four_of_a_kinds[0] + others[0]


def _score_full_house(hand):
    card_values = map(card_value, hand)
    pairs = [x for x, y in collections.Counter(card_values).items() if y == 2]
    if len(pairs) != 1:
        return 0
    three_of_a_kinds = [x for x, y in collections.Counter(card_values).items() if y == 3]
    if len(three_of_a_kinds) != 1:
        return 0

    return 1012000 + 10000 * three_of_a_kinds[0] + 10 * pairs[0]


def _score_flush(hand):
    card_values = map(card_value, hand)
    suites = set(map(card_suite, hand))
    if len(suites) != 1:
        return 0
    return 880000 + _score_values(card_values)


def _score_straight(hand):
    card_values = map(card_value, hand)
    card_values.sort()
    for i in range(len(card_values) - 1):
        if card_values[i] + 1 != card_values[i + 1]:
            return 0
    return 750000 + _score_values(card_values)


def _score_three_of_a_kind(hand):
    card_values = map(card_value, hand)
    pairs = [x for x, y in collections.Counter(card_values).items() if y == 3]
    if len(pairs) != 1:
        return 0
    others = [x for x, y in collections.Counter(card_values).items() if y == 1]

    return 600000 + 3000 * pairs[0] + _score_values(others)


def _score_two_pairs(hand):
    card_values = map(card_value, hand)
    pairs = [x for x, y in collections.Counter(card_values).items() if y == 2]
    if len(pairs) != 2:
        return 0

    others = [x for x, y in collections.Counter(card_values).items() if y == 1]
    return 520000 + 200 * pairs[0] + 200 * pairs[1] + _score_values(others)


def _score_one_pair(hand):
    card_values = map(card_value, hand)
    pairs = [x for x, y in collections.Counter(card_values).items() if y == 2]
    if len(pairs) != 1:
        return 0

    others = [x for x, y in collections.Counter(card_values).items() if y == 1]
    return 130000 + 20000 * pairs[0] + _score_values(others)
        


def _score_high_card(hand):
    card_values = map(card_value, hand)
    return _score_values(card_values)



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

def _score_values(values):
    values.sort()

    multiplier = 10000
    score = 0

    while len(values) > 0:
        val = values.pop()
        if not val:
            break
        val -= 2
        score += multiplier * val
        multiplier /= 10
    return score

def tmp_score_hand(hand):
    card_values = map(card_value, hand)
    return _score_values2(card_values)

def _score_values2(values):
    values.sort()
    multiplier = 10000
    score = 0

    while len(values) > 0:
        val = values.pop()
        if not val:
            break
        val -= 2
        print "  +", val, "*", multiplier, "=", score, "+", multiplier * val, "=", score + multiplier * val
        score += multiplier * val
        multiplier /= 10
    print "=> ", score
    return score


class Test(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(14, card_value('AD'))

        # tmp_score_hand(parse('5H 5C 6S 7S KD'))
        # tmp_score_hand(parse('2C 3S 8S 8D TD'))


        self.assertFalse(player1_wins([parse('5H 5C 6S 7S KD'), parse('2C 3S 8S 8D TD')]))
        self.assertTrue(player1_wins([parse('5D 8C 9S JS AC'), parse('2C 5C 7D 8S QH')]))
        self.assertFalse(player1_wins([parse('2D 9C AS AH AC'), parse('3D 6D 7D TD QD')]))
        self.assertTrue(player1_wins([parse('4D 6S 9H QH QC'), parse('3D 6D 7H QD QS')]))
        self.assertTrue(player1_wins([parse('2H 2D 4C 4D 4S'), parse('3C 3D 3S 9S 9D')]))
        pass
    
    def test_score_values(self):
        ace_high = ['2D', '3C', '4S', '5S', 'AC']
        king_high = ['8D', '9C', 'JS', 'QS', 'KC']
        self.assertGreater(score_hand(ace_high), score_hand(king_high))

    def test_limits(self):
        test_hands = {
            '01 worst high card possible':  ['2D', '3C', '4S', '5S', '7C'],
            '02 best high card possible': ['9D', 'JC', 'QS', 'KS', 'AC'],
            '03 worst one-pair possible': ['2D', '2C', '3S', '4S', '5C'],
            '04 best one-pair possible': ['AD', 'AC', 'KS', 'QS', 'JC'],
            '05 worst two-pair possible': ['2D', '2C', '3S', '3S', '4C'],
            '06 best two-pair possible': ['AD', 'AC', 'KS', 'KS', 'QC'],
            '07 worst three of a kind possible': ['2D', '2C', '2S', '3S', '4D'],
            '08 best three of a kind possible': ['AD', 'AC', 'AS', 'KS', 'QD'],
            '09 worst straight possible': ['2D', '3C', '4S', '5S', '6D'],
            '10 best straight possible': ['AD', 'KC', 'QS', 'JD', 'TD'],
            '11 worst flush possible': ['2D', '3D', '4D', '5D', '7D'],
            '12 best flush possible': ['AS', 'KS', 'QS', 'JS', '9S'],
            '13 worst full house possible': ['2D', '2S', '2C', '3S', '3D'],
            '14 best full house possible': ['AD', 'AS', 'AC', 'KS', 'KD'],
            '15 worst four of a kind possible': ['2D', '2S', '2C', '2S', '3D'],
            '16 best four of a kind possible': ['AD', 'AS', 'AC', 'AS', 'KD'],
            '17 worst straight-flush possible': ['2D', '3D', '4D', '5D', '6D'],
            '18 best straight-flush possible': ['KD', 'QD', 'JD', 'TD', '9D'],
            '19 royal flush': ['AD', 'KD', 'QD', 'JD', 'TD']
        }

        keys = test_hands.keys()
        keys.sort()

        last = 0
        for key in keys:
            score = score_hand(test_hands[key])
            # print str(score) + ":", key
            self.assertGreater(score, last)
            last = score
        

    def test_answer(self):
        self.assertEqual(369, solve())
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
