class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        score = 0

        for num in nums:
            if num < k:
                score += 1

        return score