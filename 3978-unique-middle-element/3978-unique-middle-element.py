class Solution(object):
    def isMiddleElementUnique(self, nums):
        a=(0+len(nums))//2
        return nums.count(nums[a])==1
        