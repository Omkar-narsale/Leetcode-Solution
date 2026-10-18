class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        MOD = 10**9 + 7
        count = 0
        n = len(arr)

        for i in range(n):
            freq = {}

            for j in range(i + 1, n):
                required = target - arr[i] - arr[j]

                if required in freq:
                    count += freq[required]

                freq[arr[j]] = freq.get(arr[j], 0) + 1

        return count % MOD