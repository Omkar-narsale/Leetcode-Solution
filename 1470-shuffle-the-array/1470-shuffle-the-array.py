class Solution(object):
    def shuffle(self, nums, n):
        mid=len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        result=[]
        for i in range(mid):
            result.append(left[i])
            result.append(right[i])
        return result
        