class Solution(object):
    def judgeSquareSum(self, c):
        left = 0
        right = int(c ** 0.5)

        while left <= right:
            total = left * left + right * right

            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1

        return False