class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        prefix = 0
        prefix_map = {0: -1}
        minimum = len(nums)

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p

            required = (prefix - target) % p

            if required in prefix_map:
                length = i - prefix_map[required]
                minimum = min(minimum, length)

            prefix_map[prefix] = i

        return minimum if minimum < len(nums) else -1