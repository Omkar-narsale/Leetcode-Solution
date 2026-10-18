class Solution:
    def smallestRangeII(self, nums: list[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        result = nums[-1] - nums[0]

        for i in range(n - 1):
            minimum = min(nums[0] + k, nums[i + 1] - k)
            maximum = max(nums[i] + k, nums[-1] - k)

            difference = maximum - minimum
            result = min(result, difference)

        return result