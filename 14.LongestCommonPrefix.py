__author__ = 'amow'
class Solution:
    # @return a string
    def find_pre(self, str1, str2):
        for i in range(0, min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                if i:
                    return str1[:i]
                else:
                    return ""
        return str1[:min(len(str1), len(str2))]

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        pref = 0
        for s in strs:
            if pref == 0:
                pref = s
                continue
            pref = self.find_pre(pref, s)
            if not pref:
                return ""
        return pref