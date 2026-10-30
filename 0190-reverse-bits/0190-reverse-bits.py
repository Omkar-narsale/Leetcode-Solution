class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:].zfill(32)

        rev = binary[::-1]

        decimal = int(rev, 2)

        return decimal