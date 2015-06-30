__author__ = 'amow'
class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        base, num = 1, 0
        for i in s[::-1]:
            num += (ord(i) - 64) * base
            base *= 26
        return num