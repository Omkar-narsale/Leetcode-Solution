class Solution(object):
    def maximizeSum(self, nums, k):
        total=0
        maximum=max(nums)
        for i in range(k):
            total+=maximum
            maximum+=1
        return total

            