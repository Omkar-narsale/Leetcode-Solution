class Solution:
    def minMoves(self, nums: List[int]) -> int:
        moves=0
        max_val=max(nums)
        for i in range(len(nums)):
            moves+=abs(nums[i]-max_val)
        return moves

      
    
