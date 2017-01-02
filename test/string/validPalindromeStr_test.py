'''
Created on Nov 15, 2016

@author: songjiguo
'''
import unittest

from src.string import validPalindromeStr as tc

class Test(unittest.TestCase):

    def testOk(self):        
        p = tc.solution()
        self.assertTrue(p.isvalidPalindromeStr("A man, a plan, a canal: Panama"))        

    def testFail(self):        
        p = tc.solution()
        self.assertFalse(p.isvalidPalindromeStr("AAAAAASFSDFSDASLJLJLL"))        

    def testZero(self):        
        p = tc.solution()
        self.assertTrue(p.isvalidPalindromeStr(""))        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()