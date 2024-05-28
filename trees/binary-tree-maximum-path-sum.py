""" Binary Tree Maximum Path Sum
A path in a binary tree is a sequence of nodes 
where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, 
return the maximum path sum of any non-empty path.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val

        def DFS(node):
            leftSum = 0
            if node.left:
                leftSum = DFS(node.left)
            rightSum = 0
            if node.right:
                rightSum = DFS(node.right)

            takeLeftSum = leftSum + node.val 
            takeRightSum = rightSum + node.val
            rootSum = leftSum + rightSum + node.val

            bestPath = max((node.val, takeLeftSum, takeRightSum))
            self.maxSum = max((self.maxSum, bestPath, rootSum))

            return bestPath
        
        DFS(root)
        return self.maxSum