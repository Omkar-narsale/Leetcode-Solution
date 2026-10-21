class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        ans=[]
        from collections import Counter
        freq=Counter(arr)
        for nums,count in freq.items():
            if count==1:
                ans.append(nums)
        if len(ans)>=k:
            return(ans[k-1])
        else:
            return ''
