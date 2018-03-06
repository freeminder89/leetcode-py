class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        rotated = True
        while start <= end:
            if rotated and nums[start] < nums[end]:  # rotated
                rotated = False
            center = (start + end) / 2
            if nums[center] == target:
                return center
            elif center == start:
                return -1 if nums[end] != target else end
            elif nums[center] > target:
                if nums[center] > nums[end] >= target:
                    start = center
                else:
                    end = center
            else:
                if nums[center] < nums[start] <= target:
                    end = center
                else:
                    start = center



sol = Solution()
test = [4,5,6,7,8,1,2,3]
for i in range(len(test)):
    print  i == sol.search(test, test[i])
print sol.search(test, 3)