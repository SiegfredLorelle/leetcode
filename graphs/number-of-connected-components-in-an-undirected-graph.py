"""Number of Connected Components in an Undirected Graph

There is an undirected graph with n nodes. 
There is also an edges array, where 
edges[i] = [a, b] means that 
there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.
"""

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n

        adjList = [[] for _ in range(n)]
        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)

        visited = set()
        def dfs(node):
            visited.add(node)
            for connNode in adjList[node]:
                if connNode in visited:
                    continue
                dfs(connNode)

        res = 0
        for node in range(n):
            if node in visited:
                continue
            dfs(node)
            res += 1
        
        return res