class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        min_val=min(nums)
        max_val=max(nums)
        for num in nums:
            if min_val<num<max_val:
                return num
        else:
            return -1