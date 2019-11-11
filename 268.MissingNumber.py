class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        result = None
        l = len(nums)
        for i in xrange(l):
            if result is None:
                result = nums[i]
            else:
                result ^= nums[i]
            result ^= i
        return result ^ l