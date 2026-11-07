from collections import Counter

class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        prefix = set()
        freq = Counter(nums)
        suffix = set(nums)
        ans = []

        for num in nums:
            prefix.add(num)

            freq[num] -= 1

            if freq[num] == 0:
                suffix.remove(num)

            diff = len(prefix) - len(suffix)
            ans.append(diff)

        return ans