class Solution:
    def countLargestGroup(self, n: int) -> int:
        freq = {}

        for num in range(1, n + 1):
            digit_sum = sum(int(d) for d in str(num))

            freq[digit_sum] = freq.get(digit_sum, 0) + 1

        maximum = max(freq.values())

        count = 0
        for value in freq.values():
            if value == maximum:
                count += 1

        return count