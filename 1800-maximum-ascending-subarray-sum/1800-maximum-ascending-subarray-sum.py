class Solution(object):
    def maxAscendingSum(self, nums):
        c_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                c_sum += nums[i]
            else:
                c_sum = nums[i]

            if c_sum > max_sum:
                max_sum = c_sum

        return max_sum