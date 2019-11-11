# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 5


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s, e = 1, n
        while s <= e:
            mid = (s + e) / 2
            if isBadVersion(mid):
                e = mid - 1
            else:
                s = mid + 1
        return s


s = Solution()
for i in range(5, 14):
    print i, s.firstBadVersion(i)