class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        first = nums[-1]
        second = nums[-2]
        return (first-1)*(second-1)