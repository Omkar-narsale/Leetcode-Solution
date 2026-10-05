class Solution(object):
    def sortEvenOdd(self, nums):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # Even indices → ascending
                if i % 2 == 0 and j % 2 == 0:
                    if nums[i] > nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                # Odd indices → descending
                if i % 2 == 1 and j % 2 == 1:
                    if nums[i] < nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
        return nums