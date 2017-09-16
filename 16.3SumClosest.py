class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        nums_len = len(nums)
        closest = 0
        min_diff = 0
        for i in xrange(nums_len - 2):
            start, end = i + 1, nums_len - 1
            while start < end:
                sum_all = nums[i] + nums[start] + nums[end]
                diff = target - sum_all
                diff = -diff if diff < 0 else diff
                if min_diff == 0 or diff < min_diff:
                    min_diff = diff
                    closest = sum_all
                if sum_all > target:
                    end -= 1
                elif sum_all < target:
                    start += 1
                else:
                    return target
        return closest
