class Solution:
    def maxFreqSum(self, s: str) -> int:
        from collections import Counter

        freq = Counter(s)
        v = []
        c = []

        for char, count in freq.items():
            if char in "aeiou":
                v.append(count)
            else:
                c.append(count)

        return max(v,default=0) + max(c,default=0)