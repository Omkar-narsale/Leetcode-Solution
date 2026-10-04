class Solution(object):
    def majorityElement(self, nums):
        from collections import Counter
        result = []
        freq = Counter(nums)
        for num, count in freq.items():
            if count > len(nums) // 3:
                result.append(num)
        return result
