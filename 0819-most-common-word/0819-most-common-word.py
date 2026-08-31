class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import string
        from collections import Counter

        paragraph = paragraph.lower()

        paragraph = paragraph.translate(
            str.maketrans(string.punctuation, ' ' * len(string.punctuation))
        )

        words = paragraph.split()

        frequency = Counter()

        for word in words:
            if word not in banned:
                frequency[word] += 1

        return frequency.most_common(1)[0][0]