class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        count=0
        for i in range(left,right+1):
            word=words[i]

            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                count+=1
        return count