class Solution(object):
    def maximumGap(self, nums):
        if len(nums)<2:
            return 0
        nums.sort()
        max_diff=0
        for i in range(1,len(nums)):
            diff=nums[i]-nums[i-1]
            if diff>max_diff:
                max_diff=diff
        return max_diff