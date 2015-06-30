__author__ = 'amow'
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        i = 0
        while n / 5:
            i += n/5
            n /= 5
        return i