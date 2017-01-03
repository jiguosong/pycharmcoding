import unittest

import test.tree.MyTreeNode as Tree
from tree import deleteBSTnode

class Test(unittest.TestCase):
    def test1(self):
        tc = deleteBSTnode.solution()
        head = Tree.TreeNode(2)
        head.left = Tree.TreeNode(1)
        head.right = Tree.TreeNode(3)
        tc.deleteBSTNode(head, 2)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

