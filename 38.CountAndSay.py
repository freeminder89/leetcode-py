__author__ = 'amow'
class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        if not n:
            return ""
        s = "1"
        for i in range(n-1):
            m, cnt, t = "", 0, ""
            for c in s:
                if c != m:
                    if m:
                        t += str(cnt) + m
                    m = c
                    cnt = 1
                else:
                    cnt += 1
            t += str(cnt) + m
            s = t
        return s