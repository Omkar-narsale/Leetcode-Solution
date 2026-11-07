class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                return nums2[j]-nums1[i]
