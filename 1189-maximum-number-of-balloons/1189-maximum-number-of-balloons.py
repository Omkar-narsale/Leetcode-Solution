class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        r=[]
        text_freq=Counter(text)
        b_freq=Counter('balloon')
        for char,count in b_freq.items():
            r.append(text_freq[char]//count)
        return min(r)
