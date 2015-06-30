__author__ = 'amow'
class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def s_comp(self, n1, n2):
        n1, n2 = int(n1), int(n2)
        if n1 > n2:
            return 1
        elif n1 < n2:
            return -1
        else:
            return 0

    def compareVersion(self, version1, version2):
        v1, v2 = version1.split("."), version2.split(".")
        mlen = min(len(v1), len(v2))
        for i in range(mlen):
            j = self.s_comp(v1[i], v2[i])
            if j:
                return j
        if len(v1) == len(v2):
            return 0
        else:
            for i in v1[mlen:]:
                if int(i):
                    return 1
            for i in v2[mlen:]:
                if int(i):
                    return -1
            return 0