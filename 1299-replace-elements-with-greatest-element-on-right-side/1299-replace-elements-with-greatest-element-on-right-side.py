class Solution(object):
    def replaceElements(self, arr):
        result=[0]*len(arr)
        great=-1
        for i in range(len(arr)-1,-1,-1):
            result[i]=great
            great=max(great,arr[i])
        return result

        