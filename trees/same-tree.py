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
        self.isSameTree = True

        def DFS(node1, node2):
            if not self.isSameTree:
                return 

            if not node1 and not node2:
                return

            if (node1 and not node2) or (not node1 and node2):
                self.isSameTree = False
                return

            if node1.val != node2.val:
                self.isSameTree = False
                return

            DFS(node1.left, node2.left)
            DFS(node1.right, node2.right)


        DFS(p, q)
        return self.isSameTree