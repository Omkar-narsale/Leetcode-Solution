class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        from collections import Counter

        freq = Counter(nums)

        for num in nums:
            if num % 2 == 0 and freq[num] == 1:
                return num

        return -1

