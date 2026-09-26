class Solution(object):
    def decompressRLElist(self, nums):
        result = []

        for i in range(0, len(nums), 2):
            frequency = nums[i]
            value = nums[i + 1]

            result.extend([value] * frequency)

        return result