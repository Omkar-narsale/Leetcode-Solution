class Solution(object):
    def isMiddleElementUnique(self, nums):
        from collections import Counter
        mid=len(nums)//2
        freq=Counter(nums)
        if freq[nums[mid]]==1:
            return True
        else:
            return False

        