class Solution(object):
    def decompressRLElist(self, nums):
        result = []

        for i in range(0, len(nums), 2):
            frequency = nums[i]
            value = nums[i + 1]

            for _ in range(frequency):
                result.append(value)

        return result