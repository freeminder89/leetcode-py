__author__ = 'amow'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {boolean}
    def isSameTree(self, p, q):
        if not q and not p:
            return True
        if q and p:
            return q.val == p.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False