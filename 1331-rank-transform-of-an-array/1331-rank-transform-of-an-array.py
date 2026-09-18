class Solution(object):
    def arrayRankTransform(self, arr):
        rank = {num: i + 1 for i, num in enumerate(sorted(set(arr)))}
        return [rank[num] for num in arr]
    