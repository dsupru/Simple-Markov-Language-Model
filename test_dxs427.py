import unittest
from test_markov import TestMarkov

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestTiles('Test for Spam task'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
