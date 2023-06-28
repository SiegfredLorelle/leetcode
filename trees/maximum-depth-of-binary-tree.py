"""Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



from typing import Optional

class Solution:
    """Solution using iterative DFS (depth-first search) using class"""
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Create a class to access instance attributes 
        # (global variable if no classes) during recursion
        class MaxDepth:
            def __init__(self):
                self.max_depth = 0

            def traverse(self, node: Optional[TreeNode], current_depth: int = 0) -> None:
                # Base case
                if not node:
                    return None

                # Update depth counters
                current_depth += 1
                if current_depth > self.max_depth:
                    self.max_depth = current_depth

                # Recursively call the children
                self.traverse(node.left, current_depth)
                self.traverse(node.right, current_depth)

        # Create instance of the class, & return the max depth after traversing
        instance = MaxDepth() 
        instance.traverse(root, 0)
        return instance.max_depth
    


# Only purpose is to create a tree from a python list for test cases
# This is not part of the solution
class tree:
    def __init__(self, elements=[]):
        if not elements:
            self.root = None
            return
        
        self.root = TreeNode(elements[0])
        prev = self.root
        nodes = []

        for element in elements[1:]:
            new_node = TreeNode(element)
            if not prev.left:
                prev.left = new_node
            elif not prev.right:
                prev.right = new_node
            else:
                prev = nodes.pop(0)
                prev.left = new_node
            nodes.append(new_node)


# Change the values in the list here to try out other test cases
test_case = tree([3,9,20,None,None,15,7])

sol = Solution()
result = sol.maxDepth(test_case.root)
print(result)
