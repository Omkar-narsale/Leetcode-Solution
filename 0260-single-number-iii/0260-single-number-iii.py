class Solution(object):
    def singleNumber(self, nums):
        from collections import Counter
        result=[]
        freq=Counter(nums)
        for num,count in freq.items():
            if count==1:
                result.append(num)
        return result
        
        