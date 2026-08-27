class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_nums = [i**2 for i in nums]
        squared_nums.sort()
        return(squared_nums)