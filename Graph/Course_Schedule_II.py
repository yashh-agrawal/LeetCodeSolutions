# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        for src, dest in prerequisites:
            adj[src].append(dest)
        
        visit = set()
        out = []

        for i in range(numCourses):
            path = set()
            if not self.dfs(i,visit,path,adj,out):
                return []
        return out
    
    def dfs(self,src,visit, path, adj, out):
        if src in path:
            return False
        if src in visit:
            return True
        visit.add(src)
        path.add(src)
        for nei in adj[src]:
            if not self.dfs(nei,visit,path,adj,out):
                return False
        path.remove(src)
        out.append(src)
        return True