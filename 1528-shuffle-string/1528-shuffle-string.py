class Solution(object):
    def restoreString(self, s, indices):
        pairs = []
        for i in range(len(s)):
            pairs.append((indices[i], s[i]))
        pairs.sort()
        result = ''
        for index, char in pairs:
            result += char
        return result