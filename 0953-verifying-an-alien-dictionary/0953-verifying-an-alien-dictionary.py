class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}
        for i in range(len(order)):
            rank[order[i]] = i
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            for j in range(min(len(word1), len(word2))):
                if rank[word1[j]] > rank[word2[j]]:
                    return False
                elif rank[word1[j]] < rank[word2[j]]:
                    break
            if word1.startswith(word2) and len(word1) > len(word2):
                return False
        return True