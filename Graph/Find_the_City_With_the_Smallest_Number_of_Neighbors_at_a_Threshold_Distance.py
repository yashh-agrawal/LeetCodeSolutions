# There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and 
# weighted edge between cities fromi and toi, and given the integer distanceThreshold.

# Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, 
# If there are multiple such cities, return the city with the greatest number.

# Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0
        
        for s,d,w in edges:
            dist[s][d] = w
            dist[d][s] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        minReachCities = float('inf')
        bestCity = -1

        for i in range(n):
            reachCity = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachCity += 1
            
            if reachCity <= minReachCities:
                minReachCities = reachCity
                bestCity = i
        return bestCity