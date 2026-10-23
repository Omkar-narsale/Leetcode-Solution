class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        i = len(num) - 1

        while k > 0:
            if i >= 0:
                k += num[i]
                num[i] = k % 10
                k //= 10
                i -= 1
            else:
                num.insert(0, k % 10)
                k //= 10

        return num