__author__ = 'amow'
class Solution:
    # @param {string} s
    # @return {boolean}
    pars = {
        "(":")", "[":"]", "{":"}"
        }
    def isValid(self, s):
        buf = []
        for i in s:
            if i in self.pars:
                buf.append(i)
            elif not buf:
                return False
            elif self.pars[buf[-1]] == i:
                buf.pop(-1)
            else:
                return False
        return len(buf) == 0