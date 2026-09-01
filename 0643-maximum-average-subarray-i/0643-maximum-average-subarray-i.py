class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        i = k

        while i < len(nums):
            window_sum = window_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum, window_sum)
            i += 1

        return max_sum / k