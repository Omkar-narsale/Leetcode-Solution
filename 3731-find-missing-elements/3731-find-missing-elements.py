class Solution(object):
    def findMissingElements(self, nums):
        m = min(nums)
        l = max(nums)
        result = []

        for i in range(m, l):
            if i not in nums:
                result.append(i)

        return result