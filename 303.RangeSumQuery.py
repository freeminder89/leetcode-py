class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.cache = []
        self.maxJ = len(nums) - 1

    def maxIntersaction(self, i, j):
        cache = None
        max_inter = 0
        for (s, e, v) in self.cache:
            if i >= e or j <= s:
                continue
            inter = min(j, e) - max(s, i)
            if inter > max_inter:
                max_inter = inter
                cache = (s, e, v)
        return cache

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        i, j = max(0, i), min(j, self.maxJ)
        cache = self.maxIntersaction(i, j)
        result = 0
        if cache:
            print "use", cache
            s, e, result = cache
            for pair in [(i, s), (e, j)]:
                factor = 1 if pair[0] < pair[1] else -1
                for idx in xrange(min(pair), max(pair) + 1):
                    result += (factor * self.nums[idx])
        else:
            for idx in xrange(i, j + 1):
                result += self.nums[idx]
        self.cache.append((i, j, result))
        return result




np = NumArray([-2, 0, 3, -5, 2, -1])
print np.sumRange(0, 2)
print np.sumRange(2, 5)
print np.sumRange(0, 5)