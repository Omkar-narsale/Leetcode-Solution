class Solution(object):
    def findRotation(self, mat, target):
        for _ in range(4):
            if mat==target:
                return True
            for i in range(len(mat)):
                for j in range(i + 1, len(mat)):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            for i in range(len(mat)):
                mat[i].reverse()
            if mat == target:
                return True
        return False