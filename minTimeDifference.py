# Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) <= 1:
            return 0
        
        times = []
        for point in timePoints:
            [hours, minutes] = point.split(':')
            time = int(minutes) + 60 * int(hours)
            times.extend([time, time + 60 * 24])
            
        times.sort()
        minDiff = sys.maxsize
        for index in range(1, len(times)):
            diff = times[index] - times[index - 1]
            minDiff = min(minDiff, diff)
            
        return minDiff
