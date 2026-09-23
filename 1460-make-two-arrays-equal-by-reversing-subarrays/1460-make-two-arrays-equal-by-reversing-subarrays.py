class Solution(object):
    def canBeEqual(self, target, arr):
        arr.sort()
        target.sort()
        return arr == target