__author__ = 'amow'
from collections import defaultdict
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        ds, dt = defaultdict(list),defaultdict(list)
        for i in range(len(s)):
            ds[s[i]].append(i)
            dt[t[i]].append(i)
        return dict([(ds[i][0], ds[i][1:]) for i in ds]) == \
               dict([(dt[i][0], dt[i][1:]) for i in dt])