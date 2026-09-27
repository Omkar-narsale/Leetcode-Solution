class Solution(object):
    def maximumCount(self, nums):
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > 0:
                right = mid
            else:
                left = mid + 1

        positive = len(nums) - left

        # Find first non-negative
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= 0:
                right = mid
            else:
                left = mid + 1

        negative = left

        return max(positive, negative)