__author__ = 'amow'
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        li = [i for i in s.split(" ") if i]
        return len(li[-1]) if li else 0