class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_c=[]
        result=[]
        for i in range(len(candies)):
            new_c.append(candies[i]+extraCandies)
            if new_c[i]>=max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
        
    