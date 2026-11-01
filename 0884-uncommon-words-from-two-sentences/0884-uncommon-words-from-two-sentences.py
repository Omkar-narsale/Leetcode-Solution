class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        r=[]
        words=s1.split()+s2.split()
        for w in words:
            if words.count(w)==1:
                r.append(w)
        return r
