class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        nums.sort()

        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1

        if k % 2 == 1:
            nums.sort(key=abs)
            nums[0] *= -1

        return sum(nums)