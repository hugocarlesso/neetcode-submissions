import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # let's first sort the stones weights
        stonesNeg = [-weight for weight in stones]
        heapq.heapify(stonesNeg)
        while len(stonesNeg) > 1 :
            current = -(-heapq.heappop(stonesNeg) - (-heapq.heappop(stonesNeg)))
            heapq.heappush(stonesNeg, current)
        stonesNeg.append(0)
        return abs(stonesNeg[0])
        
