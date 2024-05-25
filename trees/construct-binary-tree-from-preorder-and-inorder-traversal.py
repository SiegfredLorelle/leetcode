""" Construct Binary Tree from Preorder and Inorder Traversal
Given two integer arrays preorder and inorder 
where preorder is the preorder traversal of a binary tree 
and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return

        numLeftNodes = inorder.index(preorder[0]) + 1

        newNode = TreeNode()
        newNode.val = preorder[0]
        newNode.left = self.buildTree(preorder[1:numLeftNodes], inorder[:numLeftNodes - 1])
        newNode.right = self.buildTree(preorder[numLeftNodes :], inorder[numLeftNodes:])

        return newNode