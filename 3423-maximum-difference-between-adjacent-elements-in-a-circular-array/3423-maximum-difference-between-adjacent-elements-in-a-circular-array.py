class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        diff=0
        for i in range(len(nums)):
            next_index=(i+1)%len(nums)
            diff=max(diff,abs(nums[i]-nums[next_index]))
        return diff