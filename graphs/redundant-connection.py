"""Redundant Connection
In this problem, a tree is an undirected graph that 
is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, 
with one additional edge added. 
The added edge has two different vertices chosen from 1 to n, and 
was not an edge that already existed. 
The graph is represented as an array edges of length n where 
edges[i] = [ai, bi] indicates that there is an edge 
between nodes ai and bi in the graph.

Return an edge that can be removed so 
that the resulting graph is a tree of n nodes. 
If there are multiple answers, return the answer that occurs last in the input.
"""

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        rank = [1 for i in range(len(edges) + 1)]
        self.res = []

        def find(num):
            num = parents[num]
            while num != parents[num]:
                parents[num] = parents[parents[num]]
                num = parents[num]
            return num


        def union(num1, num2):
            parent1 = find(num1)
            parent2 = find(num2)
            if parent1 == parent2:
                self.res = [num1, num2]
            elif rank[parent1] > rank[parent2]:
                parents[parent2] = parent1
                rank[parent1] += rank[parent2]
            else:
                parents[parent1] = parent2
                rank[parent2] += rank[parent1]

        for node1, node2 in edges:
            union(node1, node2)
        return self.res
