# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        rowMin = []
        for i in range(n):
            rMin = float('inf')
            for j in range(m):
                rMin = min(rMin, matrix[i][j])
            rowMin.append(rMin)
        
        colMax = []
        for i in range(m):
            cMax = float('-inf')
            for j in range(n):
                cMax = max(cMax, matrix[j][i])
            colMax.append(cMax)
        
        luckyNumbers = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumbers.append(matrix[i][j])
        
        return luckyNumbers