"""
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = [True, True]
        if dividend < 0:
            positive[0] = False
            dividend = 0 - dividend
        if divisor < 0:
            positive[1] = False
            divisor = 0 - divisor
        sign = "" if positive[0] == positive[1] else "-"
        timers = [0]
        for i in range(1, 10):
            timers.append(divisor + timers[i-1])
        holder = ""
        result = ""
        for i in str(dividend):
            holder += i
            current = int(holder)
            for j in range(1, 10):
                if timers[j] > current:
                    j -= 1
                    break
            result += str(j)
            holder = str(current - timers[j])
        result = int(sign + result)
        return 2147483647 if result > 2147483647 else result