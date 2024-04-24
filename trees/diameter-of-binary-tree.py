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
        maxDiameter = 0

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            nonlocal maxDiameter
            
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            diameter = leftHeight + rightHeight
            if maxDiameter < diameter:
                maxDiameter = diameter

            longerHeight = leftHeight
            if leftHeight < rightHeight:
                longerHeight = rightHeight

            return 1 + longerHeight

        dfs(root)
        return maxDiameter
