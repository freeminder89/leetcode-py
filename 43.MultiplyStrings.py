class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if "0" in [num1, num2]:
            return "0"
        result = []
        p = -1
        for i in num2[::-1]:
            q = p
            holder = 0
            for j in num1[::-1]:
                m = int(i) * int(j) + holder
                if len(result) >= -q:
                    m += int(result[q])
                    result[q] = str(m % 10)
                else:
                    result.insert(0, str(m % 10))
                holder = m/10
                q -= 1
            if holder:
                result.insert(0, str(holder))
            p -= 1
        return "".join(result)



print Solution().multiply("0", "103")
