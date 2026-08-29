class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter

        freq = Counter(words[0])

        for word in words[1:]:
            freq = freq & Counter(word)

        result = []

        for char, count in freq.items():
            result.extend([char] * count)

        return result
