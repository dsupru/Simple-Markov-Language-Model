import unittest
import os
import math
import dxs427

class TestMarkov(unittest.TestCase):

    def test_can_get_internal_repr(self):
        ham_dir = "homework4_data/train/ham/"
        self.assertSequenceEqual(
                ['of', 'my', 'outstanding', 'mail'],
                dxs427.load_tokens(ham_dir+"ham1")[200:204],
                'can\'t parse email'
                )
        self.assertSequenceEqual(
                ['for', 'Preferences', '-', "didn't"],
                dxs427.load_tokens(ham_dir+"ham2")[110:114],
                'can\'t parse email'
                )
