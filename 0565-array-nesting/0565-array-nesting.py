class Solution:
    def arrayNesting(self, nums: list[int]) -> int:
        visited = set()
        max_count = 0

        for num in range(len(nums)):
            if num not in visited:
                current = num
                count = 0

                while current not in visited:
                    visited.add(current)
                    count += 1
                    current = nums[current]

                max_count = max(max_count, count)

        return max_count