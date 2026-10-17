class Solution:
    def findLHS(self, nums: list[int]) -> int:
        from collections import Counter
        freq=Counter(nums)
        result=0
        for num in freq:
            if num+1 in freq:
                count=freq[num]+freq[num+1]
                result=max(result,count)
        return result 