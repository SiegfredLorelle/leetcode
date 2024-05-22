"""Kth Smallest Element in a BST
Given the root of a binary search tree, and an integer k, 
return the kth smallest value (1-indexed) of 
all the values of the nodes in the tree.
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr: 
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()

            k -= 1
            if not k:
                return curr.val

            curr = curr.right