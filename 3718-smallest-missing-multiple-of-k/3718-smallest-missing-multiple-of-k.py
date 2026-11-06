class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiple=set(nums)
        num=k
        while num in multiple:
            num+=k
        return num