"""Binary Tree Level Order Traversal
Given the root of a binary tree, 
return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).
"""

from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res
            
        deq = deque([root])

        while deq:
            nodes_per_lvl  = list()
            while deq:
                node = deq.popleft()
                nodes_per_lvl.append(node)

            node_values = []
            for node in nodes_per_lvl:
                node_values.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(node_values)
            
        return res
