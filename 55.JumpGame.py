class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_pos = 0
        l = len(nums)
        for i in xrange(l):
            max_pos = max(i+nums[i], max_pos)
            if max_pos >= l:
                return True
            elif max_pos <= i:
                return False
        return True


#print Solution().canJump([2, 3, 1, 1, 4])
print Solution().canJump([3, 2, 1, 0, 4])
