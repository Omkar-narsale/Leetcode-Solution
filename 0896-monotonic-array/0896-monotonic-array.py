class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True

        for i in range(len(nums) - 1):
            j = i + 1

            if nums[i] > nums[j]:
                increasing = False

            if nums[i] < nums[j]:
                decreasing = False

        return increasing or decreasing
