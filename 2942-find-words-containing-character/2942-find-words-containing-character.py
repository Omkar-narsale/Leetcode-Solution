class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for index,value in enumerate(words):
            if x in value:
                ans.append(index)
        return ans