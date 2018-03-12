class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        return [
            [nums[i]] + j
            for i in range(len(nums))
            for j in self.permute(nums[:i] + nums[i+1:])
        ]


print Solution().permute([1, 2, 3])
