from collections import Counter

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        arr = []

        for i in range(len(nums) - 1):
            if nums[i] == key:
                arr.append(nums[i + 1])

        freq = Counter(arr)

        return freq.most_common(1)[0][0]