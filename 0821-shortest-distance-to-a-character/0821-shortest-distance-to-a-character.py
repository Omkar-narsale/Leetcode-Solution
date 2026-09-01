class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions = []
        for i in range(len(s)):
            if s[i] == c:
                positions.append(i)
        result = []
        for i in range(len(s)):
            min_distance = float('inf')
            for pos in positions:
                distance = abs(i - pos)
                min_distance = min(min_distance, distance)
            result.append(min_distance)
        return result