class Solution(object):
    def findDuplicate(self, nums):
        from collections import Counter
        freq=Counter(nums)
        for num,count in freq.items():
            if count>1:
                return num

        