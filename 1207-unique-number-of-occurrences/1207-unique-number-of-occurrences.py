class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        freq = Counter(arr)
        frequencies = []
        for f in freq:
            frequencies.append(freq[f])
        return len(frequencies) == len(set(frequencies))