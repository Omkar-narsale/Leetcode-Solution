class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        miss=[]
        for i in range(1,max(arr)+k+1):
            if i not in arr:
                miss.append(i)
        return(miss[k-1])