
class Solution(object):
    def foo(self, n, current, closed):
        if current == n:
            return [')'*(current-closed)]
        result = map(lambda x: '(%s' % x, self.foo(n, current+1, closed))
        if current > closed:
            result.extend(map(lambda x: ')%s' % x, self.foo(n, current, closed+1)))
        return result

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        if n == 1:
            return ['()']
        return self.foo(n, 0, 0)