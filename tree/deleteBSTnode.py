'''
delete a node from BST ans return the new BST
'''


class solution(object):
    def __init__(self):
        return

    def deleteBSTNode(self, root, key):
        if root.val < key:
            root = self.deleteBSTNode(root.right, key)
        elif root.val > key:
            root = self.deleteBSTNode(root.left, key)
        else:
            if root.left is None or root.right is None:
                root = root.right if root.right is not None else root.left
            else:
                p = root.right
                while p.left is not None:
                    p = p.left;
                root.val = p.val
                root.right = self.deleteBSTNode(root.right, p.val)
        return root
