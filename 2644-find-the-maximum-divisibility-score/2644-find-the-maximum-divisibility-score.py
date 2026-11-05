class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        max_score = -1
        ans = 0

        for j in range(len(divisors)):
            score = 0

            for i in range(len(nums)):
                if nums[i] % divisors[j] == 0:
                    score += 1

            if score > max_score:
                max_score = score
                ans = divisors[j]

            elif score == max_score:
                ans = min(ans, divisors[j])

        return ans