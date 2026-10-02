class Solution(object):
    def dominantIndex(self, nums):
        maximum = max(nums)
        max_index = nums.index(maximum)

        for i in range(len(nums)):
            if i == max_index:
                continue

            if maximum < 2 * nums[i]:
                return -1

        return max_index