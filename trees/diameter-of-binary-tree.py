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
