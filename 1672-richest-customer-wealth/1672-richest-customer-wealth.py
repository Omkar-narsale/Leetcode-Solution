class Solution(object):
    def maximumWealth(self, accounts):
        row_sum=[sum(row) for row in accounts]
        return max(row_sum)
    