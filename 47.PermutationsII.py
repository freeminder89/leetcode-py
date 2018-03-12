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
        result = []
        for i in range(len(nums)):
            if result and result[-1][0] == nums[i]:
                continue
            result.extend([
                [nums[i]] + j for j in self.permute(nums[:i] + nums[i+1:])
            ])
        return result
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        return self.permute(nums)


print Solution().permuteUnique([3, 3, 0, 3])
