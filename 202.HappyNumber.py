__author__ = 'amow'
class Solution:
    # @param {integer} n
    # @return {boolean}
    def next_num(self, n):
        i = (n%10)**2
        while n/10:
            n = n/10
            i += (n%10)**2
        return i
    def isHappy(self, n):
        self.haha = set()
        return self.isHappyInner(n)

    def isHappyInner(self, n):
        if n == 1:
            return True
        if n in self.haha:
            return False
        self.haha.add(n)
        return self.isHappyInner(self.next_num(n))