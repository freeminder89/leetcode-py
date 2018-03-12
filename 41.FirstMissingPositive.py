class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        for i in range(length):
            while 0 < nums[i] <= length and nums[i] != i + 1:
                p = nums[i] - 1
                if nums[p] == p + 1:
                    break
                nums[i], nums[p] = nums[p], nums[i]
        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1


print Solution().firstMissingPositive([1,1])
print Solution().firstMissingPositive([3,4,-1,1])