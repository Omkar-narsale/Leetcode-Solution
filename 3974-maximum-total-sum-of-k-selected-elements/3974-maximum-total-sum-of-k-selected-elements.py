class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort()
        total = 0

        for i in range(len(nums) - 1, len(nums) - k - 1, -1):
            total += nums[i] * max(1, mul)
            mul -= 1

        return total