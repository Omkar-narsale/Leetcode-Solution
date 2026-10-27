class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        ele_total=sum(nums)
        dig_tot=0
        for num in nums:
            for digit in str(num):
                dig_tot+=int(digit)
        return abs(ele_total-dig_tot)
