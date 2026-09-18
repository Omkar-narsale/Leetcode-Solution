class Solution(object):
    def createTargetArray(self, nums, index):
        result=[]

        for i in range(len(nums)):
            result.insert(index[i], nums[i])

        return result