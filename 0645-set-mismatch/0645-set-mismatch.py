class Solution:
    def findErrorNums(self, nums):
        dup, missing = -1, -1
        
        for i in range(1, len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                dup = i
            elif count == 0:
                missing = i
        
        return [dup, missing]

