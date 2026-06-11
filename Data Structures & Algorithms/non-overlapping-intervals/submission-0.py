class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # First we sort the intervals by start 
        intervals.sort()
        result = 0
        prevEnd = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] >= prevEnd:
                prevEnd = interval[1]
            else:
                result+=1
                prevEnd = min(interval[1], prevEnd)
        return result