class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for start, end in intervals[1:]:
            if result == [] or result[-1][1] < start:
                result.append([start, end])
            
            else:
                result[-1][1] = max(result[-1][1], end)
        return result

    



# intervals = [[1,3],[1,5],[6,7]]
# S

# |----|
#         |------|
#             |--------|
#          |---|