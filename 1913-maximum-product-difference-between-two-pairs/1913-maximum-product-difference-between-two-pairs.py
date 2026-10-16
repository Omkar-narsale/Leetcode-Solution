class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()

        max_product = nums[-1] * nums[-2]
        min_product = nums[0] * nums[1]

        return max_product - min_product