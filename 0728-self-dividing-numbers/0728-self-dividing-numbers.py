class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        new = []

        for i in range(left, right + 1):
            temp = i

            while temp > 0:
                digit = temp % 10

                if digit == 0 or i % digit != 0:
                    break

                temp //= 10

            else:
                new.append(i)

        return new


