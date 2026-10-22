class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        count = 0

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                count += 1

                if count > 1:
                    return False

                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]

        return True