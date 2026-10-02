class Solution(object):
    def dominantIndex(self, nums):
        maximum = max(nums)
        for i in range(len(nums)):
            if nums[i] == maximum:
                continue
            if maximum < 2 * nums[i]:
                return -1
        return nums.index(maximum)