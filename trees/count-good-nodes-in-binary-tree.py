""" Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good 
if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.numOfGoodNodes = 0

        def DFS(node, maxValFromRoot):
            if node.val >= maxValFromRoot:
                self.numOfGoodNodes += 1
                maxValFromRoot = node.val

            if node.left:
                DFS(node.left, maxValFromRoot)
            if node.right:
                DFS(node.right, maxValFromRoot)
            
        DFS(root, float("-inf"))
        return self.numOfGoodNodes