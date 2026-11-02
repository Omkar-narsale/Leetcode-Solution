class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        common = set(nums1) & set(nums2)

        if common:
            return min(common)

        a = min(nums1)
        b = min(nums2)

        return min(a * 10 + b, b * 10 + a)