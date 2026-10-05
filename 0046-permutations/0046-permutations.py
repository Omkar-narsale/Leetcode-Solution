class Solution(object):
    def permute(self, nums):
        from itertools import permutations
        all_perms = permutations(nums)
        result = []
        for p in all_perms:
            result.append(list(p))
        return result