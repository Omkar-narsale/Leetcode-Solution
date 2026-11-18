from collections import Counter

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        f1 = Counter(word1)
        f2 = Counter(word2)

        chars = set(word1 + word2)

        for char in chars:
            if abs(f1[char] - f2[char]) > 3:
                return False

        return True