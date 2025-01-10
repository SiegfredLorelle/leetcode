"""Clone Graph
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains 
a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
} 
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

import collections
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        clones = {node.val: Node(val=node.val, neighbors=[])} # {value: node}
        queue = collections.deque([node])

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(val=neighbor.val)
                    queue.append(neighbor)
                clones[curr.val].neighbors.append(clones[neighbor.val])

        return clones[node.val]
