"""Subtree of Another Tree
Given the roots of two binary trees root and subRoot, return true if there is 
a subtree of root with the same structure and node values of subRoot and 
false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and 
all of this node's descendants. The tree tree could also be considered as 
a subtree of itself.
"""

from typings import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return None

        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        isLeftSubtree = self.isSubtree(root.left, subRoot) 
        isRightSubtree = self.isSubtree(root.right, subRoot)
        return isLeftSubtree or isRightSubtree


    def isSameTree(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        if node1.val != node2.val:
            return False
        
        isSameLeftSubNode = self.isSameTree(node1.left, node2.left)
        isSameRightSubNode = self.isSameTree(node1.right, node2.right)
        return isSameLeftSubNode and isSameRightSubNode