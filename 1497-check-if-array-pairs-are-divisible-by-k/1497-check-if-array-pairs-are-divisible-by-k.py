class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = [0] * k

        for num in arr:
            rem = num % k
            freq[rem] += 1

        if freq[0] % 2 != 0:
            return False

        for r in range(1, (k+1)//2):
            if freq[r] != freq[k-r]:
                return False

        if k % 2 == 0 and freq[k//2] % 2 != 0:
            return False

        return True