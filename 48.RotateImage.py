class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) <= 1:
            return matrix
        start, end = 0, len(matrix) - 1
        while start < end:
            for i in range(start, end):
                (
                    matrix[start][i],
                    matrix[i][end],
                    matrix[end][end - i + start],
                    matrix[end - i + start][start]
                ) = (
                    matrix[end - i + start][start],
                    matrix[start][i],
                    matrix[i][end],
                    matrix[end][end - i + start]
                )
            start += 1
            end -= 1
        return matrix


print Solution().rotate([
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
])
