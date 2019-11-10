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

    def test_can_ngram_empty_input(self):
        self.assertSequenceEqual(
                [(('<START>', '<START>'), '<END>')],
                dxs427.ngrams(3, []),
                'can\'t parse empty n_grams.'
                )

    def test_can_get_probability_of_a_token_given_context(self):
        m = dxs427.NgramModel(1)
        m.update("a b c d")
        m.update("a b a b")
        self.assertEqual(
                0.3,
                m.prob((), "a"),
                'can\'t get token probabilities.'
                )
        self.assertEqual(
                0.1,
                m.prob((), "c"),
                'can\'t get token probabilities.'
                )
        self.assertEqual(
                0.2,
                m.prob((), "<END>"),
                'can\'t get token probabilities.'
                )
    def test_can_get_probability_2_given_context(self):
        m = dxs427.NgramModel(2)
        m.update("a b c d")
        m.update("a b a b")
        self.assertEqual(
                1,
                m.prob(("<START>",), "a"),
                'can\'t get 2 probabilities.'
                )
        self.assertEqual(
                0.3333333333333333,
                m.prob(("b",), "c"),
                'can\'t get 2 probabilities.'
                )
        self.assertEqual(
                0.0,
                m.prob(("a",), "x"),
                'can\'t get 2 probabilities.'
                )
