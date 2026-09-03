class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        minimum = min(nums)

        answer = max(0, maximum - minimum - 2*k)

        return answer