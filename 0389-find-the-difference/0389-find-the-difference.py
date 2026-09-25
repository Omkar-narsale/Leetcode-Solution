from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        sc = Counter(s)
        tc = Counter(t)

        for char in tc:
            if tc[char] > sc[char]:
                return char