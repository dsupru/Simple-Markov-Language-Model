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
