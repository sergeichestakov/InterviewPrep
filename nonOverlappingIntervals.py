# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e
#
# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0

        #Sort by end time and count all conflicts
        intervals.sort(key=lambda x: x.end)
        curr = intervals[0]
        count = 0
        for interval in intervals[1:]:
            if interval.start < curr.end: #Overlap so add to count and dont update
                count += 1
            else: #Update
                curr = interval

        return count
