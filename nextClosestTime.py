# Given a time represented in the format "HH:MM",
# form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.
class Solution:
    def nextClosestTime(self,time):
        """
        :type time: str
        :rtype: str
        """
        s = set(time)
        hours, minutes = map(int, time.split(':')) #Extract hours/minutes and convert to int
        while True:
            if minutes == 59: #Increment minutes
                minutes = 0
                hours = 0 if hours == 23 else hours + 1 #Increment hours
            else:
                minutes += 1

            time = '{:02d}:{:02d}'.format(hours, minutes)
            if set(time).issubset(s): #Every element in new time is in old time
                return time
        return time

