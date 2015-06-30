__author__ = 'amow'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums, init=True):
        if not nums:
            return 0
        if init:
            self.data = {0:0, 1:nums[-1], 2:max(nums[-2:])}
        t = len(nums)
        if t not in self.data:
            self.data[t] = max(nums[0] + self.rob(nums[2:], False), self.rob(nums[1:], False))
        return self.data[t]