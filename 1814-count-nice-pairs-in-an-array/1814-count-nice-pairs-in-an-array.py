class Solution:
    def countNicePairs(self, nums: list[int]) -> int:
        from collections import Counter

        freq = Counter()

        for num in nums:
            value = num - int(str(num)[::-1])
            freq[value] += 1

        count = 0

        for f in freq.values():
            count += f * (f - 1) // 2

        return count % (10**9 + 7)