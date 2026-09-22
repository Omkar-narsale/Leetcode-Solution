class Solution(object):
    def findDuplicates(self, nums):
        from collections import Counter
        
        freq = Counter(nums)
        result = []

        for num, count in freq.items():
            if count > 1:
                result.append(num)

        return result