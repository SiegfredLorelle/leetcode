""" Validate Binary Search Tree
Given the root of a binary tree, determine 
if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains 
only nodes with keys less than the node's key.
- The right subtree of a node contains 
only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""

from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValidBST = True
        def DFS(node, lowerBound, upperBound):
            if  not self.isValidBST:
                return

            if not (lowerBound < node.val < upperBound):
                self.isValidBST = False
            
            if node.left:
                DFS(node.left, lowerBound, node.val)
            if node.right:
                DFS(node.right, node.val, upperBound)
        
        DFS(root, float("-inf"), float("+inf"))
        return self.isValidBST