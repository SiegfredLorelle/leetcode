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
        """ SOLUTION USING DFS: quadratic space and time (n^2) """
        # if not inorder or not preorder:
        #     return

        # numLeftNodes = inorder.index(preorder[0]) + 1

        # newNode = TreeNode()
        # newNode.val = preorder[0]
        # newNode.left = self.buildTree(preorder[1:numLeftNodes], inorder[:numLeftNodes - 1])
        # newNode.right = self.buildTree(preorder[numLeftNodes :], inorder[numLeftNodes:])

        # return newNode
    
        """ SOLUTION USING DFS: linear space and time (n) """
        # Inorder values mapping to its index
        inIdxs = {num: idx for idx, num in enumerate(inorder)}
        # Preorder index, used for during dfs traversal
        self.preIdx = 0

        def dfs(start, end):
            # Base case
            if start > end:
                return

            # Get the middle, separates left vals and right vals
            mid = inIdxs[preorder[self.preIdx]]
            
            # Build the node
            node = TreeNode(preorder[self.preIdx])
            self.preIdx += 1
            node.left = dfs(start, mid - 1)
            node.right = dfs(mid + 1, end)
            return node   
        
        return dfs(0, len(preorder) - 1)