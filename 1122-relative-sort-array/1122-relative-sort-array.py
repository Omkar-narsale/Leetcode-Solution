class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        new=[]
        freq=Counter(arr1)
        for num in arr2:
            new.extend([num]*freq[num])

        remaning=[]
        for num in freq:
            if num not in arr2:
                remaning.extend([num]*freq[num])
        remaning.sort()
        new.extend(remaning)
        return new
