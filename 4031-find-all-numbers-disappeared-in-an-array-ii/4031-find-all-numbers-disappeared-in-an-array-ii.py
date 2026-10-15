class Solution(object):
    def findDisappearedNumbers(self, nums, lower, upper):
        nums_set = set(nums)
        result = []
        start = None
        end = None

        for i in range(lower, upper + 1):
            if i not in nums_set:
                if start is None:
                    start = i
                end = i
            else:
                if start is not None:
                    result.append([start, end])
                    start = None
                    end = None

        if start is not None:
            result.append([start, end])

        return result