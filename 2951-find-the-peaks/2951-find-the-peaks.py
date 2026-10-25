class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        result = []

        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                result.append(i)

        return result