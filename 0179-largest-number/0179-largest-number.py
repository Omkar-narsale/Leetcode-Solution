class Solution(object):
    def largestNumber(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if str(nums[j]) + str(nums[i]) > str(nums[i]) + str(nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]
        result = ""
        for num in nums:
            result += str(num)
        if result[0] == "0":
            return "0"
        return result
        