class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter
        freq=Counter(nums)
        max_f=max(freq.values())
        total=sum(f for f in freq.values() if f==max_f)
        return total
