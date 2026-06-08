class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        totalIslands = 0

        def dfs(row, col):
            #if we exceed the grid we should exit
            if row >= rows or row < 0 or col >= cols or col <0:
                return 
            #if we encounter a 0 we should exit:
            if grid[row][col] =="0":
                return
            # else we change the ones in 0 to avoid counting them twice
            grid[row][col] = "0"

            dfs(row+1,col) #Down
            dfs(row, col+1) #Right
            dfs(row, col-1) #Left
            dfs(row-1, col) #Up

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row,col)
                    totalIslands +=1
        return totalIslands
