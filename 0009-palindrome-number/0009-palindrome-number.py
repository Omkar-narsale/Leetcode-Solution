class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = str(x)[::-1]

        if str(x) == rev:
            return True
        else:
            return False