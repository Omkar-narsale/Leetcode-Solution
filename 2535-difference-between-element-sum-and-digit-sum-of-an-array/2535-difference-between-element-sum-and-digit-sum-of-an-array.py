class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        ele_total=sum(nums)
        dig=[]
        for num in nums:
            for digit in str(num):
                dig.append(int(digit))
        dig_tot=sum(dig)
        return abs(ele_total-dig_tot)
