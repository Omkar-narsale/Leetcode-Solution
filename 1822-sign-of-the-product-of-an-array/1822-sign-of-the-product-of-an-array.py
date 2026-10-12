class Solution(object):
    def arraySign(self, nums):
        prod = 1

        for num in nums:
            prod *= num

        if prod > 0:
            return 1
        elif prod < 0:
            return -1
        else:
            return 0