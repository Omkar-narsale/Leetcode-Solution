class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        s=sorted(nums)
        rank={}
        for i in range(len(s)):
            if s[i] not in rank:
                rank[s[i]]=i
        result=[]
        for num in nums:
            result.append(rank[num])
        return result
        