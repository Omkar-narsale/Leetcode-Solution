class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter
        freq=Counter(s)
        return len(set(freq.values()))==1 