class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        k=0
        count=0
        for i in range (len(nums)):
            if nums[i]==0:
                count=0
            else:
                count+=1
            
            if count>k:
                k=count
        return k