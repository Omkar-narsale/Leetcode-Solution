class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            temp = nums[i]
            d_sum = 0

            while temp > 0:
                d_sum += temp % 10
                temp = temp // 10

            if d_sum == i:
                return i

        return -1