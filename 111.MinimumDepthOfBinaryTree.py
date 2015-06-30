__author__ = 'amow'
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if not root:
            return 0
        self.nodes = [root]
        cnt = 1
        while 1:
            tl = []
            for n in self.nodes:
                if not n.left and not n.right:
                    return cnt
                if n.left:
                    tl.append(n.left)
                if n.right:
                    tl.append(n.right)
            self.nodes = tl
            cnt += 1