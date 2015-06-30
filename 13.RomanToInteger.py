__author__ = 'amow'
class Solution:
    # @param s, a string
    # @return a boolean
    conf = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    minus = {
        "I": "VX", "X": "LC", "C": "DM",
    }
    conts = {
        "I": 3,
        "X": 3,
        "C": 3,
        "V": 1,
        "L": 1,
        "D": 1,
        "M": 3,
    }
    def romanToInt(self, s):
        ret = 0
        prec = ""
        prec_count = 0
        for i in range(0, len(s)):
            if prec == s[i]:
                prec_count += 1
            else:
                prec = s[i]
                prec_count = 1
            if prec_count > self.conts[prec]:
                return 0
            if i == len(s) - 1:
                ret += self.conf[s[i]]
            elif self.conf[s[i]] >= self.conf[s[i+1]]:
                ret += self.conf[s[i]]
            elif prec_count > 1:
                return 0
            elif s[i] in "VLD":
                return 0
            elif s[i+1] not in self.minus[s[i]]:
                return 0
            else:
                ret -= self.conf[s[i]]
        return ret