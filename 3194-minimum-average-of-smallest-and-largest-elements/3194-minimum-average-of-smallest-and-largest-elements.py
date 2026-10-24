class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        nums.sort()
        ans=[]
        while nums:
            smallest=nums.pop(0)
            largest=nums.pop()
            avg=(smallest+largest)/2
            ans.append(avg)
        return min(ans)
        