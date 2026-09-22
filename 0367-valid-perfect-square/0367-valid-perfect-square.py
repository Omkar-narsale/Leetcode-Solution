class Solution(object):
    def isPerfectSquare(self, num):
        left = 0
        right = num

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1

        return False