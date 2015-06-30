__author__ = 'amow'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        j = nums[0]
        cnt = 0
        for i in nums:
            if j==i:
                cnt += 1
            elif cnt > n >> 1:
                break
            else :
                j = i
                cnt = 1
        return j