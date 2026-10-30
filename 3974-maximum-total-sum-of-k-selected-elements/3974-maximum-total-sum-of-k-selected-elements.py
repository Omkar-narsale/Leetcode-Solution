class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort()
        selected = nums[-k:]

        total = 0

        for num in reversed(selected):
            total += num * max(1, mul)
            mul -= 1

        return total