'''
Created on Nov 15, 2016

@author: songjiguo
'''
import unittest

from others import rotate_array as tc


class Test(unittest.TestCase):
    def testOK(self):
        p = tc.rotateArray_solution()
        s = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 1, 2, 3, 4]
        p.rotateArray(s, k)
        self.assertEqual(s, expected, "they must be equal")

    def testBad(self):
        p = tc.rotateArray_solution()
        s = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [6, 7, 1, 2, 3, 4, 5]
        p.rotateArray(s, k)
        self.assertNotEqual(s, expected, "they must be equal")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
