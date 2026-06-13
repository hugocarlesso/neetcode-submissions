"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #first sort interval in ascending order of start time
        sorted_intervals = []
        for interval in intervals:
            sorted_intervals.append((interval.start, interval.end))
        sorted_intervals.sort()
        for i in range(len(sorted_intervals) -1):
            if sorted_intervals[i][1] > sorted_intervals[i+1][0]:
                return False
        
        return True
