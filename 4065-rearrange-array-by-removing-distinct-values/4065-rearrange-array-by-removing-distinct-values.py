
from collections import Counter
class Solution:
    def rearrangeArray(self, nums):
        freq = Counter(nums)
        ans = []

        while len(ans) < len(nums):
            for num in sorted(freq):
                if freq[num] > 0:
                    ans.append(num)
                    freq[num] -= 1

        return ans

