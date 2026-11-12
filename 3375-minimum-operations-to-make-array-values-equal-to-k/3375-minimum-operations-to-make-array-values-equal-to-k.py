class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        new = set(nums)
        count = 0

        for num in new:
            if num > k:
                count += 1
            elif num < k:
                return -1

        return count