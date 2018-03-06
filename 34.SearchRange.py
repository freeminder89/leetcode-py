class Solution(object):
    def range(self, nums, target, cut_pos, start, end):
        result = [cut_pos, cut_pos]
        l_end, r_start = cut_pos, cut_pos
        while start <= l_end:
            center = (start + l_end) / 2
            if nums[center] == target:
                result[0] = center
                l_end = center - 1
            else:
                start = center + 1
        while r_start <= end:
            center = (r_start + end) / 2
            if nums[center] == target:
                result[1] = center
                r_start = center + 1
            else:
                end = center - 1
        return result


    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        if not nums:
            return result
        start, end = 0, len(nums) - 1
        while start <= end:
            center = (start + end) / 2
            if target == nums[center]:
                return self.range(nums, target, center, start, end)
            elif target < nums[center]:
                end = center - 1
            else:
                start = center + 1
        return result



print Solution().searchRange([5, 7, 7, 8, 8, 8, 10], 8)
