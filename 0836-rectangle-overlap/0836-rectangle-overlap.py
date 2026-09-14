class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        left = max(rec1[0], rec2[0])
        right = min(rec1[2], rec2[2])
        width = right - left

        bottom = max(rec1[1], rec2[1])
        top = min(rec1[3], rec2[3])
        height = top - bottom

        area = width * height

        if width > 0 and height > 0:
            return True
        else:
            return False