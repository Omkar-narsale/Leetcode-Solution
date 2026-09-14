class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        columns = []

        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    columns.append(j)

        
        for j in columns:
            for i in range(len(matrix)):
                matrix[i][j] = 0

        for i in rows:
            for j in range(len(matrix[i])):
                matrix[i][j] = 0