class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count=0
        for w in words:
            if w.startswith(pref):
                count+=1
        return count