__author__ = 'amow'
class Solution:
    # @param {integer} n
    # @return {integer}

    def countPrimes(self, n):
        if n < 3:
            return 0
        s = [1]*n
        for i in xrange(2, n):
            if i*i > n:
                break
            if not s[i]:
                continue
            j = i*i
            while j < n:
                s[j] = 0
                j += i
        return reduce(lambda x, y: x+1 if y else x, s[2:], 0)
