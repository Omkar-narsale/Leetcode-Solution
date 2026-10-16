class Solution(object):
    def findGCD(self, nums):
        import math
        return math.gcd(min(nums), max(nums))
