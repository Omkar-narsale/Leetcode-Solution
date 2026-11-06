class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        from collections import Counter
        freq=Counter(nums)
        tot=0
        for num,count in freq.items():
            if count%k==0:
                tot+=num*count
        return tot