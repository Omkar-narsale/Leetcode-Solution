class Solution(object):
    def arrayRankTransform(self, arr):
        sorted_arr=sorted(arr)
        rank={}
        result=[]
        c=1
        for i in range(len(arr)):
            if sorted_arr[i] not in rank:
                rank[sorted_arr[i]]=c
                c+=1
        for i in range(len(arr)):
            result.append(rank[arr[i]])
        return result       