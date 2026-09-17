class Solution:
    def trimMean(self, arr: list[int]) -> float:
        arr.sort()
        remove=len(arr)//20
        for _ in range(remove):
            arr.pop(0)
            arr.pop()
        mean=sum(arr)/len(arr)
        return mean