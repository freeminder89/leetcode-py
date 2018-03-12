class Solution(object):
    def calc(self, candidates, target, start, combine, result):
        if combine and not target:
            result.append([] + combine)
            return
        pre_pop = 0
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            if pre_pop == candidates[i]:
                continue
            combine.append(candidates[i])
            self.calc(candidates, target - candidates[i], i+1, combine, result)
            pre_pop = combine.pop()

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.calc(candidates, target, 0, [], result)
        return result



print Solution().combinationSum2([10,1,2,7,6,1,5], 8)