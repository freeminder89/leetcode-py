class Solution(object):
    def key(self, s):
        key = [0]*26
        for i in s:
            key[ord(i)-97] += 1
        return "".join(map(str, key))

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for s in strs:
            result.setdefault(self.key(s), []).append(s)
        return result.values()


print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
