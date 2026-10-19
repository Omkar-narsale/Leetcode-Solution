class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)

        for i in range(0, len(s), 2 * k):
            left = i
            right = min(i + k - 1, len(s) - 1)

            while left < right:
                chars[left], chars[right] = chars[right], chars[left]

                left += 1
                right -= 1

        return "".join(chars)