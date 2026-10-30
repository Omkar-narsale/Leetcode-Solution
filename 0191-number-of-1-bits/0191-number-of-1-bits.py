class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        count = binary.count('1')
        return count