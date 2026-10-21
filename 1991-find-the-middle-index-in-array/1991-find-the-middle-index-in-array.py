class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        left_sum=0
        for i in range(len(nums)):
            right_sum=total-left_sum-nums[i]
            if left_sum==right_sum:
                return i
            left_sum+=nums[i]
        return -1