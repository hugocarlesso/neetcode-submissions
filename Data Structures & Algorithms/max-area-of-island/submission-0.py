class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea= 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i,j, area):
            if i>=rows or i<0 or j>=cols or j<0  or grid[i][j] == 0:
                return area

            grid[i][j] = 0
            area +=1

            area = dfs(i, j+1, area) # Check right neighboor
            area = dfs(i, j-1, area) # Check left neighboor
            area = dfs(i-1,j, area) # Check top neighboor
            area = dfs(i+1,j, area) # Check bottom neighboor
            return area
        
        for r in range(rows):
            for c in range(cols):
                maxArea=max(maxArea, dfs(r,c,0))
        return maxArea
            


        