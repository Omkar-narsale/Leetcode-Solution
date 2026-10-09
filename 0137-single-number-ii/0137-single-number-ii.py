class Solution(object):
    def singleNumber(self, nums):
        from collections import Counter
        freq=Counter(nums)
        for num,count in freq.items():
            if count==1:
                return num
       
        