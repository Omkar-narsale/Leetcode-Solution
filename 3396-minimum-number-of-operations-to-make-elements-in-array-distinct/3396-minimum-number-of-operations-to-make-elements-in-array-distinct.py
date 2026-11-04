class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opt=0
        while len(nums)!=len(set(nums)):
            nums=nums[3:]
            opt+=1
        return opt
