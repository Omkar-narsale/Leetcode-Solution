class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid <= x:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer