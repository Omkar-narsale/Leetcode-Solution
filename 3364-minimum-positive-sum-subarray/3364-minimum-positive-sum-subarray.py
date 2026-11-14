class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        minimum = float('inf')

        for i in range(n):
            total = 0

            for j in range(i, n):
                total += nums[j]
                length = j - i + 1

                if l <= length <= r and total > 0:
                    minimum = min(minimum, total)

        return minimum if minimum != float('inf') else -1