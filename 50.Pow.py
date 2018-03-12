class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        neg = False
        if n < 0:
            n *= -1
            neg = True
        if n == 1:
            base = x
        else:
            tail = x if n % 2 else 1
            half = self.myPow(x, n/2)
            base = half * half * tail
        return (1.0/base) if neg else base


print Solution().myPow(0.2, -1)