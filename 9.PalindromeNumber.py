__author__ = 'amow'
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if type(x) is long or x<0:
            return False
        return x == self.reverse(x)
    def reverse(self, x):
        ret = 0
        while(x):
            ret *= 10
            ret += x % 10
            x /= 10
        return ret