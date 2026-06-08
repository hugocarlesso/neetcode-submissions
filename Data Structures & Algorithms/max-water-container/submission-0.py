class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        start = 0
        end = 1
        for start in range(len(heights)):
            for end in range(start +1 , len(heights)):

                # area is equal to height * width
                width = (end - start)
                height = min(heights[start], heights[end])
                currentArea = width * height
                # update maxArea if currentArea is bigger than maxArea
                maxArea = max(maxArea, currentArea)

        return maxArea
        
