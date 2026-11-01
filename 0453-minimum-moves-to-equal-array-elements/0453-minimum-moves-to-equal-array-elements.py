class Solution:
    def minMoves(self, nums: list[int]) -> int:
        moves = sum(nums) - min(nums) * len(nums)
        return moves