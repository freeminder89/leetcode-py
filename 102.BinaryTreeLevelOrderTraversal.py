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
    def levelOrder(self, root):
        if not root:
            return []
        ret = []
        nodes = [root]
        while nodes:
            vl, nl = [], []
            for n in nodes:
                vl.append(n.val)
                if n.left:
                    nl.append(n.left)
                if n.right:
                    nl.append(n.right)
            ret.append(vl)
            nodes = nl
        return ret
