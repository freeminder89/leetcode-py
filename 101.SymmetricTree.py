__author__ = 'amow'
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        elif not (root.left and root.right):
            return False
        root.left.right, root.right.left, root.right.right = \
        root.right.right, root.left.right, root.right.left
        return root.left.val == root.right.val and self.isSymmetric(root.left) and self.isSymmetric(root.right)