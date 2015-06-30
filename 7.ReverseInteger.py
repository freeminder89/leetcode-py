__author__ = 'amow'
class Solution:
    # @return an integer
    def reverse(self, x):
        ret = 0
        nag = x < 0
        x = int(abs(x))
        if type(x) is long:
            return 0
        while(x):
            ret *= 10
            ret += x % 10
            x /= 10
        if type(ret) is long:
            return 0
        return -1*ret if nag else ret