'''
Created on Nov 15, 2016

@author: songjiguo
'''
import itertools
import unittest

from combinatorics.src import permutation as tc


class Test(unittest.TestCase):
    def testOk(self):
        p = tc.solution()
        nums = [1, 2, 3]
        res = p.permute(nums)
        tmp = list(itertools.permutations(nums))
        expected = [list(x) for x in tmp]
        self.assertEqual(res, expected)

    def testFail(self):
        p = tc.solution()
        nums = [1, 2, 3]
        res = p.permute(nums)
        tmp = list(itertools.permutations(nums))
        expected = [list(x) for x in tmp]
        del expected[2]
        self.assertNotEqual(res, expected)

    def testLarge(self):
        p = tc.solution()
        nums = [4, 3, 7, 1, 8, 7, 45, 3]
        res = p.permute(nums)
        tmp = list(itertools.permutations(nums))
        expected = [list(x) for x in tmp]
        self.assertEqual(res, expected)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
