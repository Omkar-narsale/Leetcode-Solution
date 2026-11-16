class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            total = 0
            for d in str(n):
                total += int(d) ** 2

            n = total

        return True