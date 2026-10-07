class Solution(object):
    def sumOfGoodNumbers(self, nums, k):
        total = 0
        for i in range(len(nums)):
            left = i - k
            right = i + k
            left_good = left < 0 or nums[i] > nums[left]
            right_good = right >= len(nums) or nums[i] > nums[right]
            if left_good and right_good:
                total += nums[i]
        return total    