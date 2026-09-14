class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=nums1+nums2
        sorted_lst = sorted(merged)
        n=(len(merged))
        mid=n//2
        
        if n%2==0:
            return (sorted_lst[mid - 1] + sorted_lst[mid]) / 2
        else:
            return sorted_lst[mid]