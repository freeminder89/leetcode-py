__author__ = 'amow'
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        i = 0
        bit_len = 0
        while n :
            bit_len += 1
            i = i << 1
            if n%2:
                i += 1
            n = n/2
        for j in range(bit_len, 32):
            i = i << 1
        return i