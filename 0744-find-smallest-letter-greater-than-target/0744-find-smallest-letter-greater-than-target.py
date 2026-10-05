class Solution(object):
    def nextGreatestLetter(self, letters, target):
        for letter in letters:
            if letter > target:
                return letter 
        else:
            return letters[0]
        
    
        