class Solution:
    def countDaysTogether(self, a: str, b: str, c: str, d: str) -> int:
        def f(s):
            m, q = int(s[:2]), int(s[3:])
            return (275 * m) // 9 - 2 * ((m + 9) // 12) + q - 30

        return max(0, min(f(b), f(d)) - max(f(a), f(c)) + 1)
