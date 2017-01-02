'''
Created on Nov 16, 2016

@author: songjiguo
'''
import unittest

from src.string import zigzagconversion as tc

class Test(unittest.TestCase):

    def testOk(self):
        p = tc.solution()   # after instance, the method is boind, No need for self
        s = 'PAYPALISHIRING'
        expected = 'PAHNAPLSIIGYIR'
        self.assertEqual(expected, p.convert(s, 3))

    def testEmpty(self):
        p = tc.solution()   # after instance, the method is boind, No need for self
        s = ''
        expected = ''
        self.assertEqual(expected, p.convert(s, 3))

    def testOne(self):
        p = tc.solution()   # after instance, the method is boind, No need for self
        s = 'PAYPALISHIRING'
        expected = 'PAYPALISHIRING'
        self.assertEqual(expected, p.convert(s, 1))        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
