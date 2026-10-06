class Solution(object):
    def groupAnagrams(self, strs):
        from collections import Counter
        result = {}
        for words in strs:
            freq = Counter(words)
            key = tuple(sorted(freq.items()))
            if key not in result:
                result[key] = []
            result[key].append(words)
        return list(result.values())
       
        