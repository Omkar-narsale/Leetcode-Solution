class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        r=Counter(ransomNote)
        m=Counter(magazine)
        for char,count in r.items():
            if m[char]<count:
                return False
        else:
            return True
        