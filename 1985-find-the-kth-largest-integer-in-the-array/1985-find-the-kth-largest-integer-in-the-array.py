class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums.sort(key=int)
        return(nums[-k])