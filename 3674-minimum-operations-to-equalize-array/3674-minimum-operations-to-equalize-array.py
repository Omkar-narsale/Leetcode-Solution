class Solution:
    def minOperations(self, nums: List[int]) -> int:
        for num in nums:
            if num != nums[0]:
                return 1

        return 0