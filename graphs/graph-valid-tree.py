"""Graph Valid Tree - Explanation
Given n nodes labeled from 0 to n - 1 and a 
list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {num: set() for num in range(n)}
        for node1, node2 in edges:
            adjList[node1].add(node2)
            adjList[node2].add(node1)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for child in adjList[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n