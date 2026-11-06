class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = {}
        good = 0
        n = len(nums)

        for i in range(n):
            diff = nums[i] - i

            good += freq.get(diff, 0)

            freq[diff] = freq.get(diff, 0) + 1

        total = n * (n - 1) // 2

        return total - good