class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        from collections import Counter
        freq1=Counter(words1)
        freq2=Counter(words2)
        count=0
        for word in freq1:
            if freq1[word]==1 and freq2[word]==1:
                count+=1
        return count