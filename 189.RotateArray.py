__author__ = 'amow'
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.

    def rotate(self, nums, k):
        n = len(nums)
        if k > n:
            k = k % n
        nums.reverse()
        for i in xrange(n):
            j = k - i - 1 if i < k else n - 1 - (i - k)
            if j > i:
                nums[j], nums[i] = nums[i], nums[j]