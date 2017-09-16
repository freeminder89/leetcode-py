class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.nSum(nums, target, 4)

    def nSum(self, nums, target, n):
        self.nums_length = len(nums)
        if self.nums_length < n:
            return []
        nums.sort()
        self.nums = nums
        return self.lockPrevious(n, target, 0, [])

    def nextUnequal(self, index, direction):
        step = direction
        while 0 <= index + step <= self.nums_length - 1 and self.nums[index] == self.nums[index + step]:
            step += direction
        return step

    def twoSum(self, start, target, chosen):
        end = self.nums_length - 1
        result = []
        while start < end:
            _sum = self.nums[start] + self.nums[end]
            if _sum == target:
                result.append(chosen + [self.nums[start], self.nums[end]])
                end += self.nextUnequal(end, -1)
                start += self.nextUnequal(start, 1)
            elif _sum > target:
                end += self.nextUnequal(end, -1)
            else:
                start += self.nextUnequal(start, 1)
        return result

    def lockPrevious(self, addend_count, target, start, pre_hold):
        if addend_count == 2:
            return self.twoSum(start, target, pre_hold)
        if target > addend_count * self.nums[-1]:
            return []
        result = []
        for i in range(start, self.nums_length - addend_count + 1):
            if target < addend_count * self.nums[i]:
                break
            if i > start and self.nums[i] == self.nums[i - 1]:
                continue
            r = self.lockPrevious(addend_count - 1, target - self.nums[i], i + 1, pre_hold + [self.nums[i]])
            if r:
                result.extend(r)
        return result
