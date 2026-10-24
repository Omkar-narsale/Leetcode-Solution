class Solution:
    def minimumAverage(self, nums: list[int]) -> float:
        nums.sort()
        averages = []

        while nums:
            smallest = nums.pop(0)
            largest = nums.pop()

            avg = (smallest + largest) / 2
            averages.append(avg)

        return min(averages)