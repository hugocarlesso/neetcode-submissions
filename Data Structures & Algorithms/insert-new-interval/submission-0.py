class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = 0
        n = len(intervals) -1

        i = 1
        res = []

        for i in range(len(intervals)):
            
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]

            elif newInterval[0] > intervals[i][1]: 
                res.append(intervals[i])
            
            #overlapping
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        
        res.append(newInterval)
        return res

