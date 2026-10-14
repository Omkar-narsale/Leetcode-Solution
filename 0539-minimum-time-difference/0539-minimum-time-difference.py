class Solution(object):
    def findMinDifference(self, timePoints):
        minutes = []

        for time in timePoints:
            hours, mins = time.split(":")
            total = int(hours) * 60 + int(mins)
            minutes.append(total)

        minutes.sort()

        result = 1440

        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            result = min(result, diff)

        circular_diff = 1440 - minutes[-1] + minutes[0]
        result = min(result, circular_diff)

        return result