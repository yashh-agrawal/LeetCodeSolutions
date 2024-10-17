# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        result = []

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    result.append((i,j))
                else:
                    mat[i][j] = '#'
        
        for row, col in result:
            for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
                
                new_row = row + dx
                new_col = col + dy

                if 0 <= new_row < n and 0 <= new_col < m and mat[new_row][new_col] == '#':
                    mat[new_row][new_col] = mat[row][col]+1
                    result.append((new_row,new_col))
        return mat