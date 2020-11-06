##Leetcode November 2020
#Day 4: Minimum Height Trees 
#Input: n = 4, edges = [[1,0],[1,2],[1,3]]
#Output: [1]
#Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        def maxpath(v, visited):
            visited.add(v)
            path = [maxpath(n, visited) for n in adj[v] if n not in visited]
            path = max(path or [[]], key= len)
            path.append(v)
            return path
        
        x=0
        path = maxpath(x, set())
        y = path[0]
        path = maxpath(y, set())
        m = len(path)
        return path[(m-1)//2:m//2+1]
        