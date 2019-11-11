class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        pos = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                if pos != i:
                    nums[pos] = nums[i]
                pos += 1
        for j in xrange(pos, len(nums)):
            nums[j] = 0
