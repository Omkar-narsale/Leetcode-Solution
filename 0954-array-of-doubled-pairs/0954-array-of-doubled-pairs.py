from collections import Counter
class Solution(object):
    def canReorderDoubled(self, arr):
        count = Counter(arr)
        for num in sorted(arr, key=abs):
            if count[num] == 0:
                continue
            if count[2 * num] == 0:
                return False
            count[num] -= 1
            count[2 * num] -= 1
        return True