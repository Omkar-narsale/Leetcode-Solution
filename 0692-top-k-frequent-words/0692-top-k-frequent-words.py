class Solution(object):
    def topKFrequent(self, words, k):
        from collections import Counter
        freq = Counter(words)
        result = sorted(
            freq.keys(),
            key=lambda word: (-freq[word], word)
        )
        return result[:k]