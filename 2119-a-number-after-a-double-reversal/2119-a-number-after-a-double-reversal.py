class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        # Convert to string, reverse, then convert to int to drop leading zeros
        reversed_num = int(str(num)[::-1])
        reversed_num2 = int(str(reversed_num)[::-1])
        
        return reversed_num2 == num
