class Solution:
    def countElements(self, nums: list[int]) -> int:
        min_val=min(nums)
        max_val=max(nums)
        if min_val==max_val:
            return 0
        count=0 
        for num in nums:
            if min_val<num<max_val:
                count+=1
        return count