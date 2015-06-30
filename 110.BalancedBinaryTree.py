__author__ = 'amow'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}

    def calc_depth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        ld, rd = self.calc_depth(root.left), self.calc_depth(root.right)
        if -1 in (ld, rd) or abs(ld-rd) > 1:
            return -1
        return max(ld, rd) + 1

    def isBalanced(self, root):
        return self.calc_depth(root) >= 0