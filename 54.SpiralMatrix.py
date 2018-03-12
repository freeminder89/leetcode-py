class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        if not n:
            return []
        h, v, i, j = 1, 0, 0, 0
        if n == 1:  # 1 column must start with vertical move
            h, v = v, h
        result = []
        count = 0
        while count < m * n:
            result.append(matrix[i][j])
            count += 1
            if h:  # horizontal
                if min(i, m - i - 1) <= j + h <= n - min(i, m - i - 1) - 1:
                    j += h
                else:  # turn
                    v, h = h, 0
                    i += v
            else:  # vertical
                if min(j, n - j - 1) < i + v <= m - min(j, n - j - 1) - 1:
                    i += v
                else:  # turn
                    v, h = 0, -v
                    j += h
        return result


print Solution().spiralOrder([
    [1, 2, 3, 10],
    [4, 5, 6, 11],
    [7, 8, 9, 12]
])
