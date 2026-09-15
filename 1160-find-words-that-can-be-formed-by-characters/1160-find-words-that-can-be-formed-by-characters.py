from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        freq = Counter(chars)
        total = 0

        for word in words:
            freq_word = Counter(word)
            valid = True

            for char in freq_word:
                if freq_word[char] > freq[char]:
                    valid = False
                    break

            if valid:
                total += len(word)

        return total