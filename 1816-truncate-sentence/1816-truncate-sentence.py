class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # Split into words, take the first k words, and join them with a space
        return " ".join(s.split()[:k])
