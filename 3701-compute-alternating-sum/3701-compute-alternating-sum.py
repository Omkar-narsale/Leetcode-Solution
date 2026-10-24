class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        total=0
        for i in range(len(nums)):
            if i %2==0:
                total+=nums[i]
            else:
                total-=nums[i]
        return total