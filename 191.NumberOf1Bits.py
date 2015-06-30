__author__ = 'amow'
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        i = 0
        while n:
            if n % 2:
                i += 1
            n = n/2
        return i