class Solution:
    def canAliceWin(self, n: int) -> bool:
        count = 10
        turns = 0

        while n >= count:
            n -= count
            count -= 1
            turns += 1

        return turns % 2 == 1