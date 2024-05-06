""" Binary Tree Right Side View
Given the root of a binary tree, 
imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.
"""

from typing import Optional, List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        valueOfNodesFromRight = [root.val]
        nodesPerLevel = []

        while queue:
            nodesPerLevel.clear()

            while queue:
                node = queue.popleft()
                if node.left:
                    nodesPerLevel.append(node.left)
                if node.right:
                    nodesPerLevel.append(node.right)

            for node in nodesPerLevel:
                queue.append(node)
            
            if queue:
                valueOfNodesFromRight.append(queue[-1].val)

        return valueOfNodesFromRight