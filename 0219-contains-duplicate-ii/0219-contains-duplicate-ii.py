class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i in range(len(nums)):
            if nums[i] in seen:
                if i - seen[nums[i]] <= k:
                    return True

            seen[nums[i]] = i

        return False