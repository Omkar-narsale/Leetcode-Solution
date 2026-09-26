class Solution(object):
    def distinctAverages(self, nums):
        nums.sort()
        averages = []

        while len(nums) > 0:
            minimum = nums.pop(0)
            maximum = nums.pop()
            avg = (minimum + maximum) / 2.0
            averages.append(avg)

        return len(set(averages))