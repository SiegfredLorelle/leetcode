""" Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two 
nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges 
between them.
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0

        def DFS(node):
            maxLeft = 0
            maxRight = 0
            if node.left:
                maxLeft = DFS(node.left)
            if node.right:
                maxRight = DFS(node.right)

            diameter = maxLeft + maxRight
            if diameter > self.diameter:
                self.diameter = diameter
            
            return max(maxLeft, maxRight) + 1


        DFS(root)
        return self.diameter
