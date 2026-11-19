
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        from collections import Counter

        freq = Counter(nums)
        need = Counter()

        for num in nums:
            if freq[num] == 0:
                continue

            freq[num] -= 1

            if need[num] > 0:
                need[num] -= 1
                need[num + 1] += 1

            else:
                if freq[num + 1] > 0 and freq[num + 2] > 0:
                    freq[num + 1] -= 1
                    freq[num + 2] -= 1
                    need[num + 3] += 1
                else:
                    return False

        return True
