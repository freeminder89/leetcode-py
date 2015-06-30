__author__ = 'amow'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @param {integer} sum
    # @return {boolean}

    def calc_vals(self, root, sum):
        if not root.left and not root.right:
            return sum == root.val
        if root.left and self.calc_vals(root.left, sum - root.val):
            return True
        if root.right and self.calc_vals(root.right, sum - root.val):
            return True
        return False

    def hasPathSum(self, root, sum):
        if not root:
            return False
        return self.calc_vals(root, sum)