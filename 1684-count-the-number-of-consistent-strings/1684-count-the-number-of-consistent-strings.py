class Solution(object):
    def countConsistentStrings(self, allowed, words):
        count=0
        for w in words:
            if all (char in allowed for char in w):
                count+=1
        return count