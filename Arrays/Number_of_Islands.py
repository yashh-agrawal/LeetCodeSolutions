# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        def dfs(i,j):
            if i < 0 or i>=len(grid) or j< 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
        
        numbers_of_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    numbers_of_islands+=1
                    dfs(i,j)
        
        return numbers_of_islands