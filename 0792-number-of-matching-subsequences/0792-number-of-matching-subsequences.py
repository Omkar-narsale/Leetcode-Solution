class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        from collections import Counter
        word_freq=Counter(words)
        result=0
        for word,freq in word_freq.items():
            i=0
            for char in word:
                i=s.find(char,i)

                if i==-1:
                    break
                i+=1

            else:
                result+=freq
        return result      

        
        