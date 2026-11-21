class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        from collections import Counter

        freq = Counter(nums)
        max_freq = max(freq.values())

        first = {}
        last = {}

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i

        minimum = float('inf')

        for num in freq:
            if freq[num] == max_freq:
                length = last[num] - first[num] + 1
                minimum = min(minimum, length)

        return minimum