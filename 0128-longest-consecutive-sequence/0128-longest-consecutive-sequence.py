class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not  nums:
            return 0
        count=1
        maximum=1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]-nums[i-1]==1:
                count+=1
            else:
                count=1
            maximum=max(maximum,count)
        return maximum

    
