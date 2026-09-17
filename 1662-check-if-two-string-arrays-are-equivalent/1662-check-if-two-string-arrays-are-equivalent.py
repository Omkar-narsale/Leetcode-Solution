class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        n1=''.join(word1)
        n2=''.join(word2)
        if n1==n2:
            return True
        else:
            return False
        