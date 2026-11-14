class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits=[int(d) for d in str(n)]
        import math
        return math.prod(digits)-sum(digits)