class Solution(object):
    def sumOfUnique(self, nums):
        total=0
        from collections import Counter
        freq=Counter(nums)
        for num,count in freq.items():
            if count==1:
                total=total+num
        return total
        
        