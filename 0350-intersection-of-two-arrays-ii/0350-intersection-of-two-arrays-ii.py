class Solution:
    def intersect(self, nums1, nums2):
        freq = {}
        
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1
        
        result = []
        
        for num in nums2:
            if freq.get(num, 0) > 0:
                result.append(num)
                freq[num] -= 1
        
        return result