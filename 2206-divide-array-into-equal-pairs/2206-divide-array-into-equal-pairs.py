class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        from collections import Counter
        freq=Counter(nums)
        for num,count in freq.items():
            if count%2!=0:
                return False
        return True
        