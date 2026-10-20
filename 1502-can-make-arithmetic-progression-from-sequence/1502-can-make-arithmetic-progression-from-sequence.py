class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff=arr[1]-arr[0]
        for i in range(1,len(arr)-1):
            if arr[i+1]-arr[i] !=diff:
                return False
        return True