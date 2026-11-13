class Solution:
    def findValidElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        leftmax = [0] * n
        rightmax = [0] * n

        leftmax[0] = float('-inf')
        rightmax[-1] = float('-inf')

        for i in range(1, n):
            leftmax[i] = max(leftmax[i-1], nums[i-1])

        for i in range(n-2, -1, -1):
            rightmax[i] = max(rightmax[i+1], nums[i+1])

        ans = []

        for i in range(n):
            if nums[i] > leftmax[i] or nums[i] > rightmax[i]:
                ans.append(nums[i])

        return ans