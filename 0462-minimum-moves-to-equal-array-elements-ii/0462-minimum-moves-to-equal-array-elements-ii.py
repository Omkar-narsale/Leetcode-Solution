class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        target=nums[len(nums)//2]
        moves=0
        for num in nums:
            moves+=abs(num-target)
        return moves

       
        