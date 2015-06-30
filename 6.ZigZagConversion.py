__author__ = 'amow'
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if not s or nRows == 1:
            return s
        step = (nRows - 1) * 2
        outs = ""
        for i in range(nRows):
            j = i
            mstep = step - i * 2
            while True:
                if j >= len(s):
                    break
                outs += s[j]
                if 0 < i < nRows - 1:
                    j += mstep
                    mstep = step - mstep
                else:
                    j += step
        return outs