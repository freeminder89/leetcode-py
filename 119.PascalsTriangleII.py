__author__ = 'amow'
class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        rowIndex += 1
        k = rowIndex/2 + rowIndex%2
        ret = [0] * k
        ret[0] = 1
        for i in xrange(rowIndex):
            c = 0
            for j in xrange((i+1)/2 + (i+1)%2):
                if not ret[j]:
                    ret[j] = 2*c
                else:
                    t = ret[j]
                    ret[j] += c
                    c = t
        return ret + (ret[-2::-1] if rowIndex%2 else ret[::-1])