__author__ = 'amow'
class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        s = []
        while n:
            s.append(chr(65 + ((n-1) % 26)))
            n = (n-1)/26
        return "".join(s[::-1])