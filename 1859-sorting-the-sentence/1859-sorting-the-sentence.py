class Solution:
    def sortSentence(self, s: str) -> str:
        ans = [""] * len(s.split())

        for word in s.split():
            pos = int(word[-1])
            act = word[:-1]

            ans[pos-1] = act

        return " ".join(ans)