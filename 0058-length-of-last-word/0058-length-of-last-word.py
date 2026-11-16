class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new=list(s.split())
        return len(new[-1])