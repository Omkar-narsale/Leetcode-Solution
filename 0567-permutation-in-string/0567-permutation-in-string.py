class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)

        for i in range(len(s2)):
            window = s2[i:i + len(s1)]

            if Counter(window) == freq:
                return True

        return False