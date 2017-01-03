import unittest
from collections import deque

from list.src import add2number as tc


class Test(unittest.TestCase):
    def testName(self):
        s = tc.solution()
        a = deque([2, 4, 3])
        b = deque([5, 6, 4])
        c = deque([7, 0, 8])
        res = s.add2number(a, b)
        self.assertEqual(c, res)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
