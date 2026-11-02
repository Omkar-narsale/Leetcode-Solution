class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        s_freq=Counter(s)
        t_freq=Counter(t)
        steps=0
        for char in s_freq:
            if t_freq[char]<s_freq[char]:
                steps+=s_freq[char]-t_freq[char]
        return steps