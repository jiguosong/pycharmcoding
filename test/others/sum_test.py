import unittest

from others import sum as tc

class Test(unittest.TestCase):
    def testOK(self):
        p = tc.solution()
        nums = [2, 7, 11, 15]
        target = 9
        inx1, inx2 = p.twosum(nums, target)
        self.assertEqual(nums[inx1 - 1] + nums[inx2 - 1], target, msg="must be equal")

    def testFail(self):
        p = tc.solution()
        nums = [2, 7, 11, 15]
        target = 10;
        inx1, inx2 = p.twosum(nums, target)
        self.assertEqual(inx1, -1)
        self.assertEqual(inx2, -1)

    def testZero(self):
        p = tc.solution()
        nums = []
        target = 10;
        inx1, inx2 = p.twosum(nums, target)
        self.assertEqual(inx1, -1)
        self.assertEqual(inx2, -1)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
