class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        min=prices[0]
        for i in range (1,len(prices)):
            profit=prices[i]-min
            if (profit>ans):
                ans=profit
            if(prices[i]<min):
                min=prices[i]
        return ans
