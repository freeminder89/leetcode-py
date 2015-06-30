__author__ = 'amow'
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n < 1:
            return 0
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            a, b = b, a + b
        return b
