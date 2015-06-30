__author__ = 'amow'
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        j = -1
        for i in xrange(len(nums)):
            if nums[i] == val:
                if j < 0:
                    j = i
            elif j >= 0:
                nums[j] = nums[i]
                j += 1
        return j if j > -1 else len(nums)