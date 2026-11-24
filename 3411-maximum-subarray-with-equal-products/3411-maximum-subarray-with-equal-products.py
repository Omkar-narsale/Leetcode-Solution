class Solution:
    def maxLength(self, nums: List[int]) -> int:
        import math

        maximum = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sub = nums[i:j]

                product = math.prod(sub)
                gcd = math.gcd(*sub)
                lcm = math.lcm(*sub)

                if product == gcd * lcm:
                    maximum = max(maximum, len(sub))

        return maximum