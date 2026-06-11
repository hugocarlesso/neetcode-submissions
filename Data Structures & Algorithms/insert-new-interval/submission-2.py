class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # starting of new interval is > than end of current interval 
        while i < n and newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
            i+=1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        result.append(newInterval)

        return result + intervals[i:]


                    
                    
"""
|------|
            |----|
                  |---|
                        |-----|
         |----------|

                         |----|
              |-------------|
and we want to add 
         |-|
at step 1 new interval can be fully before any others,
 fully after, 
 overlapping and lasting before end of current
 overlapping and lasting longer than previously
"""

