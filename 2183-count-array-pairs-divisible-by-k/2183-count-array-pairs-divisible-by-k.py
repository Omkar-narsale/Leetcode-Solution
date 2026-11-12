class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        import math 
        freq={}
        count=0
        for num in nums:
            g=math.gcd(num,k)

            for prev_g,f in freq.items():
                if (prev_g*g)%k==0:
                    count+=f    
            freq[g] = freq.get(g, 0) + 1
        return count