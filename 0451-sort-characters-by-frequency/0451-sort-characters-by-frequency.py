class Solution(object):
    def frequencySort(self, s):
        from collections import Counter

        freq = Counter(s)
        result = ""

        for char, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            result += char * count

        return result