class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:
            original=original*2
        return original
        