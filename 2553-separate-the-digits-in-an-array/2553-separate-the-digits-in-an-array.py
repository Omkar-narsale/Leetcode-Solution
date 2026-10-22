class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        result=[]
        for num in nums:
            for digit in str(num):
                result.append(int(digit))
        return result