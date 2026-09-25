class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True

        return False