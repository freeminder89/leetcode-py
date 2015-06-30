__author__ = 'amow'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        pre, cnt = None, 0
        for i in nums:
            if i != pre:
                nums[cnt] = i
                cnt += 1
                pre = i
        return cnt