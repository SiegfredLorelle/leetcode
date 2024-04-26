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
        isBalanced = True
        
        def dfs(node: TreeNode) -> int:
            # Base case
            if not node:
                return 0

            # Perform DFS on both left and right nodes if it exists
            # dfs(node) returns the height of that subtree/child node
            leftHeight = 0
            rightHeight = 0
            if node.left:
                leftHeight = dfs(node.left)
            if node.right:
                rightHeight = dfs(node.right)

            # Alternative way of writing getting the absolute value (abs())
            heightDiff = leftHeight - rightHeight
            if heightDiff < 0:
                heightDiff *= -1
            
            # Node is not balanced if height difference is more than 1 
            if heightDiff > 1:
                nonlocal isBalanced
                isBalanced = False

            # Get the bigger height between left and right subtree/ child node
            # Alternative way of getting the bigger value between two (max(leftHeight, rightHeight))
            biggerHeight = leftHeight
            if rightHeight > leftHeight:
                biggerHeight = rightHeight

            # Return the height of this node
            return biggerHeight + 1

        dfs(root)
        return isBalanced