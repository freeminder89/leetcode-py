# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root:
            return result
        nodes = [root]
        parents = [0]
        while nodes:
            next_level = []
            next_parents = []
            for (n, p) in zip(nodes, parents):
                if n is root:
                    result.append(str(n.val))
                else:
                    result[p] = "%s->%s" % (result[p], n.val)
                if n.left:
                    next_level.append(n.left)
                    next_parents.append(p)
                if n.right:
                    next_level.append(n.right)
                    if not n.left:
                        next_parents.append(p)
                    else:
                        result.append(result[p])
                        next_parents.append(len(result) - 1)
            nodes = next_level
            parents = next_parents
        return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

print Solution().binaryTreePaths(root)
