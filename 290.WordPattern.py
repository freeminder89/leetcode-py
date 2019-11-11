class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d = {}
        pos = 0
        end = len(str)
        seen = ""
        for s in pattern:
            wd = ""
            if pos >= end:
                return False
            while pos < end and str[pos] != " ":
                wd += str[pos]
                pos += 1
            pos += 1
            if wd in d:
                if s != d[wd]:
                    return False
            elif s in seen:
                return False
            else:
                seen += s
                d[wd] = s
        return pos >= end


s = Solution()
print s.wordPattern("abba", "dog cat cat dog")
print s.wordPattern("abba", "dog cat cat fish")
print s.wordPattern("abba", "dog dog dog dog")
print s.wordPattern("jquery", "jquery")
print s.wordPattern("aaa", "aa aa aa aa")