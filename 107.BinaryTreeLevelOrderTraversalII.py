__author__ = 'amow'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if not root:
            return []
        nodes = [root]
        ret = []
        while nodes:
            vl, nl = [], []
            for n in nodes:
                vl.append(n.val)
                if n.left:
                    nl.append(n.left)
                if n.right:
                    nl.append(n.right)
            ret.insert(0, vl)
            nodes = nl
        return ret