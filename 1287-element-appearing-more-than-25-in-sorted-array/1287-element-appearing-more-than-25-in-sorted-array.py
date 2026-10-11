class Solution(object):
    def findSpecialInteger(self, arr):
        from collections import Counter
        freq = Counter(arr)
        limit = len(arr) // 4
        for num, count in freq.items():
            if count > limit:
                return num