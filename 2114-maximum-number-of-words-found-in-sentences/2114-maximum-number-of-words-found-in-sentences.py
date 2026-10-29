class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        max_words = 0

        for words in sentences:
            w = words.split()
            max_words = max(max_words, len(w))

        return max_words

