class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea= 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i,j):
            if i>=rows or i<0 or j>=cols or j<0  or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            return 1 + dfs(i, j+1) + dfs(i, j-1) + dfs(i-1,j) + dfs(i+1,j)

        # O(m*n)--> every single cell is evaluated a maximum of 2 times
        for r in range(rows):
            for c in range(cols):
                maxArea=max(maxArea, dfs(r,c))
        return maxArea
            


        