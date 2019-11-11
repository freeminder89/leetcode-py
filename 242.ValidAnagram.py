class Solution(object):
    def key(self, s):
        key = [0]*26
        for i in s:
            key[ord(i)-97] += 1
        return "".join(map(str, key))


    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.key(s) == self.key(t)