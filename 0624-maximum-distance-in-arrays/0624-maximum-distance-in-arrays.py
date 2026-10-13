class Solution(object):
    def maxDistance(self, arrays):
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        result = 0
        for i in range(1, len(arrays)):
            distance = max(
                abs(arrays[i][-1] - min_val),
                abs(arrays[i][0] - max_val)
            )
            result = max(result, distance)

            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return result