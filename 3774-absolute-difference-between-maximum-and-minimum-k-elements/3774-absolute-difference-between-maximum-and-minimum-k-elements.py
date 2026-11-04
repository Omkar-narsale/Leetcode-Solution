class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_val=sum(nums[:-k])
        min_val=sum(nums[k:])
        return abs(max_val-min_val)