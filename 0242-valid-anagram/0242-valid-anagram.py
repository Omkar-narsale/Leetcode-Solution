class Solution(object):
    def isAnagram(self, s, t):
        from collections import Counter
        freq_s=Counter(s)
        freq_t=Counter(t)
        if freq_s == freq_t:
            return True
        return False
        