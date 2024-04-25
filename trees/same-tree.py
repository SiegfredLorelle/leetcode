"""Same Tree
Given the roots of two binary trees p and q, write a function to check if they 
are the same or not.

Two binary trees are considered the same if they are structurally identical, 
and the nodes have the same value.
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        isSame = True

        def dfs(pNode: Optional[TreeNode], qNode: Optional[TreeNode]) -> None:
            nonlocal isSame

            if not isSame:
                return

            if not pNode and not qNode:
                return

            if (not pNode and qNode) or (pNode and not qNode):
                isSame = False
                return

            if (pNode.val != qNode.val):
                isSame = False
                return
            
            dfs(pNode.left, qNode.left)
            dfs(pNode.right, qNode.right)

        dfs(p, q)
        return isSame

        