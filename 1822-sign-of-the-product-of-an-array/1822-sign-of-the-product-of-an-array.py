class Solution(object):
    def arraySign(self, nums):
        neg = 0

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                neg += 1

        if neg % 2 == 0:
            return 1
        else:
            return -1