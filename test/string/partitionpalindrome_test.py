'''
Created on Nov 15, 2016

@author: songjiguo
'''
import unittest

from src.string import partitionpalindrome as tc

class Test(unittest.TestCase):

    def testOk(self):
        p = tc.solution()
        s = "aab"
        expected = [['a', 'a', 'b'], ['aa', 'b']]
        res = p.findPartitionpalindrome(s)
        self.assertEqual(res, expected, "must be equal")
    
    def testFail(self):
        p = tc.solution()
        s = "aab"
        expected = [['a', 'b'], ['a', 'b']]
        res = p.findPartitionpalindrome(s)
        self.assertNotEqual(res, expected, "must not be equal")

    def testZero(self):
        p = tc.solution()
        s = ""
        expected = []
        res = p.findPartitionpalindrome(s)
        self.assertEqual(res, expected, "must be equal")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()