import unittest
import os
import math
import dxs427

class TestMarkov(unittest.TestCase):

    def test_can_tokenize(self):
        self.assertSequenceEqual(
                ['This', 'is', 'an', 'example', '.'],
                dxs427.tokenize(" This is an example. "),
                'can\'t tokenize string.'
                )
        self.assertSequenceEqual(
                ["'", 'Medium', '-', 'rare', ',', "'", 'she', 'said', '.'],
                dxs427.tokenize("'Medium-rare,' she said."),
                'can\'t tokenize string 2.'
                )
    def test_can_get_n_grams(self):
        self.assertSequenceEqual(
                [((), 'a'), ((), 'b'), ((), 'c'), ((), '<END>')],
                dxs427.ngrams(1, ["a", "b", "c"]),
                'can\'t parse n_grams.'
                )
        self.assertSequenceEqual(
                [(('<START>',), 'a'), (('a',), 'b'), (('b',), 'c'), (('c',), '<END>')],
                dxs427.ngrams(2, ["a", "b", "c"]),
                'can\'t parse n_grams 2.'
                )
        self.assertSequenceEqual(
                [(('<START>', '<START>'), 'a'),
                 (('<START>', 'a'), 'b'),
                 (('a', 'b'), 'c'),
                 (('b', 'c'), '<END>')],
                dxs427.ngrams(3, ["a", "b", "c"]),
                'can\'t parse n_grams 3.'
                )
