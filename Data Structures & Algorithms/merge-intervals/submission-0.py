class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first we need to sort the intervals by start time 
        intervals.sort()

        # we will iterate over the full intervals
        resu = []
        for interval in intervals:
            if not resu or resu[-1][1]< interval[0]:
                resu.append(interval)
            else:
                resu[-1][1] = max(interval[1], resu[-1][1])
        return resu

        