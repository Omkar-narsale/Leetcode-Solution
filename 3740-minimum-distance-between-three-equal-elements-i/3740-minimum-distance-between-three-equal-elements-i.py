class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dis = float('inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] == nums[j] == nums[k]:
                        total = abs(i-j) + abs(j-k) + abs(k-i)
                        dis = min(dis, total)

        return -1 if dis == float('inf') else dis