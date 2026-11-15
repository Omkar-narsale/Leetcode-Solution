class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        new = []
        total = 0

        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                new.append(arr[i:j])

        for i in range(len(new)):
            if len(new[i]) % 2 != 0:
                total += sum(new[i])

        return total