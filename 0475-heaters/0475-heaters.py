class Solution(object):
    def findRadius(self, houses, heaters):
        heaters.sort()
        max_radius = 0

        for house in houses:
            left = 0
            right = len(heaters) - 1

            while left <= right:
                mid = (left + right) // 2

                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1

            dist = float('inf')

            if left < len(heaters):
                dist = min(dist, abs(heaters[left] - house))

            if right >= 0:
                dist = min(dist, abs(heaters[right] - house))

            max_radius = max(max_radius, dist)

        return max_radius