class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        matrix_1d = [element for row in matrix for element in row]
        matrix_1d.sort()
        return matrix_1d[k-1]