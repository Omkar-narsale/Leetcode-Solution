class Solution:
  def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
    ans = float('inf')
    for i in range(len(nums)):
      if nums[i] == target:
        ans = min(ans, abs(i - start))
    return ans
