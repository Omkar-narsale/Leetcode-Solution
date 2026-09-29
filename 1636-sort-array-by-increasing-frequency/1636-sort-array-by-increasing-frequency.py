from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        freq = Counter(nums)
        new = []
        for num, count in sorted(freq.items(), key=lambda x: (x[1], -x[0])):
            new.extend([num] * count)
        return new