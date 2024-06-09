""" Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

NOTE: A height-balanced binary tree is a binary tree in which the depth of 
the two subtrees of every node never differs by more than one.
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True

        def DFS(node):
            if not node or not self.isBalanced:
                return 0

            leftMax = DFS(node.left)
            rightMax = DFS(node.right)
            
            heightDiff = abs(leftMax - rightMax)
            
            if heightDiff > 1:
                self.isBalanced = False
            
            return max(leftMax, rightMax) + 1


        DFS(root)
        return self.isBalanced