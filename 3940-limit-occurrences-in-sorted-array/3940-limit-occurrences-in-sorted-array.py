class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        from collections import Counter

        freq = Counter()
        ans = []

        for num in nums:
            if freq[num] < k:
                ans.append(num)
                freq[num] += 1

        return ans