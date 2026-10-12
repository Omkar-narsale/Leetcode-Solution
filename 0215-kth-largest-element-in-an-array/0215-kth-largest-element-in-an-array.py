class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return (nums[-k])
        