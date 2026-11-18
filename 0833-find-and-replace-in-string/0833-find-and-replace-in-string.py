class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        result = ''
        i = 0
        operations = sorted(zip(indices, sources, targets))

        while i < len(s):
            replaced = False

            for index, source, target in operations:
                if i == index:
                    if s[i:i + len(source)] == source:
                        result += target
                        i += len(source)
                        replaced = True
                        break

            if not replaced:
                result += s[i]
                i += 1

        return result