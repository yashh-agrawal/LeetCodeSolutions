# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def path_exists(u,v):

            if u == v:
                return True
            
            visited.add(u)

            for neighbor in graph[u]:
                if neighbor not in visited:
                    if path_exists(neighbor,v):
                        return True
            return False
        
        for u,v in edges:

            visited = set()
            if path_exists(u,v):
                return [u,v]
            else:
                graph[u].append(v)
                graph[v].append(u)
        return None