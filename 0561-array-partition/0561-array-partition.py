class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        for i in range(0,len(nums),2):
            window=nums[i:i+2]
            small=min(window)
            total+=small
        return total