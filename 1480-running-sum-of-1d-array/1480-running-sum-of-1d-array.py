class Solution(object):
    def runningSum(self, nums):
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
          prefix[i]=prefix[i-1]+nums[i]
        return prefix
