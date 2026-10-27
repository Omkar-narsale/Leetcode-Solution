from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        freq = Counter(nums)
        result = -1
        max_count = 0

        for num, count in freq.items():
            if num % 2 == 0:
                if count > max_count:
                    max_count = count
                    result = num
                elif count == max_count and num < result:
                    result = num

        return result