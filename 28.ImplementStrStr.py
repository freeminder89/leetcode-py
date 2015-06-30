__author__ = 'amow'
class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        nl = len(needle)
        for i in xrange(len(haystack) - nl + 1):
            if haystack[i:i+nl] == needle:
                return i
        return -1