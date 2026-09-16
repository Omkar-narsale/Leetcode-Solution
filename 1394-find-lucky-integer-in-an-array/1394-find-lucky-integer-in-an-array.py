class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        lucky=-1
        freq=Counter(arr)
        for key,value in freq.items():
            if key==value:
                if key>lucky:
                    lucky=key
        return lucky

