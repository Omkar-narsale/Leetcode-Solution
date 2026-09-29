class Solution(object):
    def minSubsequence(self, nums):
        nums.sort()
        total = sum(nums)
        result = []
        current_sum = 0
        for i in range(len(nums) - 1, -1, -1):
            current_sum += nums[i]
            result.append(nums[i])
            if current_sum > total - current_sum:
                break
        return result
        