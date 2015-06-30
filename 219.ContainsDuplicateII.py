__author__ = 'amow'
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i, None]
            elif d[nums[i]][1] is None:
                d[nums[i]][1] = i
            elif d[nums[i]][1] - d[nums[i]][0] > i - d[nums[i]][1]:
                d[nums[i]] = [d[nums[i]][1], i]
        flag = False
        for i in d:
            if d[i][1] is None:
                continue
            flag = True
            if d[i][1] - d[i][0] > k:
                return False
        return flag