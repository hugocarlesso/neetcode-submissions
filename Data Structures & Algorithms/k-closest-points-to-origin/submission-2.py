import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def computeDistance(point:List[int]):
            return sum([point[i]**2 for i in range(len(point))])
        maxHeap = []
        heapq.heapify(maxHeap)

        for point in points:
            distance = computeDistance(point)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap,(-distance, point))
            else:
                if -maxHeap[0][0] > distance:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap,(-distance, point))
        return [point for _,point in maxHeap]
        