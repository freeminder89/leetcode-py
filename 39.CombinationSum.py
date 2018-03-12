class Solution(object):
    def calc(self, candidates, target, start, combine, result):
        if combine and not target:
            result.append([] + combine)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            combine.append(candidates[i])
            self.calc(candidates, target - candidates[i], i, combine, result)
            combine.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.calc(candidates, target, 0, [], result)
        return result



print Solution().combinationSum([1, 2, 3, 4], 4)