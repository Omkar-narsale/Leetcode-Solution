class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        r = nums[::-1]
        return nums + r