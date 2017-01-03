'''
Created on Nov 15, 2016

@author: songjiguo
'''
import unittest

from dp.src import longestPalindrome as tc


class Test(unittest.TestCase):
    def testOK(self):
        p = tc.solution()
        res = p.findLongestPalindrome("bananas")
        expected = "anana"
        self.assertEqual(res, expected)

    def testFail(self):
        p = tc.solution()
        res = p.findLongestPalindrome("bananas")
        expected = "banan"
        self.assertNotEqual(res, expected)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
