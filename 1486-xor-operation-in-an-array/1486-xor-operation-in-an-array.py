class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        x=0
        for i in range(0,n):
            nums.append(start + 2 * i)
        for num in nums:
            x^=num
        return x   
