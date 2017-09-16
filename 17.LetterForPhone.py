class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        digit_to_letter = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        digit_to_letter = dict(zip([str(i) for i in range(10)], digit_to_letter))
        for d in digits:
            letters = list(digit_to_letter.get(d, ''))
            if not result:
                result = letters
            else:
                result = reduce(lambda x, y: y + x, map(lambda x: ["%s%s" % (x, l) for l in letters], result), [])
        return result
