class Solution(object):
    def centerExtend(self, s, start_index, c_length, s_len):
        if start_index == 0 or start_index + c_length >= s_len or s[start_index - 1] != s[start_index + c_length]:
            return start_index, c_length
        return self.centerExtend(s, start_index - 1, c_length + 2, s_len)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        maxl = 1
        s_len = len(s)
        for i in xrange(s_len):
            start_i, len_i = self.centerExtend(s, i, 1, s_len)
            if len_i > maxl:
                start, maxl = start_i, len_i
            if i < s_len - 1 and s[i] == s[i + 1]:
                start_i, len_i = self.centerExtend(s, i, 2, s_len)
                if len_i > maxl:
                    start, maxl = start_i, len_i
        return s[start:start + maxl]
