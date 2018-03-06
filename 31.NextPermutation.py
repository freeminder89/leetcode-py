"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
smallest greater value using same digit combination. treat smallest as next bigger of largest
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n_l = len(nums)
        if n_l == 1:
            return
        cut, swp = -1, 0
        for i in xrange(n_l - 1, 0, -1):
            if nums[i] > nums[i-1]:
                cut = i - 1
                for j in xrange(n_l - 1, cut, -1):
                    if nums[j] > nums[cut]:
                        swp = j
                        break
                break
        if cut != -1:
            nums[cut], nums[swp] = nums[swp], nums[cut]
        cut += 1
        j = n_l - 1
        while cut < j:
            nums[cut], nums[j] = nums[j], nums[cut]
            cut += 1
            j -= 1


s = Solution()
for t in [[1, 2, 3], [3, 2, 1], [1, 1, 5], [3, 4, 5, 2, 1]]:
    s.nextPermutation(t)
    print  t
