class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        count=1
        maximum=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                count=1

            if count>maximum:
                maximum=max(maximum,count)
        return maximum           
       