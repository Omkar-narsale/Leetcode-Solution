class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count1 = 0
        count2 = 0
        for i in nums1:
            if i in nums2:
                count1 += 1
        for i in nums2:
            if i in nums1:
                count2 += 1
        return [count1, count2]