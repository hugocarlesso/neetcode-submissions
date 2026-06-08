class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = {}
        # compute distance of every point to origin
        # index match between keys of distances and index in points
        for i, point in enumerate(points):
            distances[i] = (point[0] **2 + point[1] **2)**0.5

        sorted_distances = sorted(distances.items(), key= lambda x: x[1])
        sorted_indexes = [sorted_distance[0] for sorted_distance in sorted_distances][:k]
        result = [points[i] for i in sorted_indexes]
        return result
        