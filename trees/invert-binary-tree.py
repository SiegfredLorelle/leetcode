# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # This is only added to view the result of the solution
    def convert_to_list(self):
        """ Converts binary tree into python list. 
        The binary tree is read in BFS (breadth-first-search)
        """
        new_list = [self.val]
        prev = self
        current = self.left
        nodes = []
        
        while current:
            new_list.append(current.val)
            nodes.append(current)

            if current == prev.left:
                current = prev.right
            else:
                prev = nodes.pop(0)
                current = prev.left

        return new_list



from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root or (not root.left and not root.right):
            return None

        root.left, root.right = root.right, root.left

        if root.left:
            self.invertTree(root.left)
        if root.right:
            self.invertTree(root.right)

        return root
    
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
test_case = tree([4,2,7,1,3,6,9])

sol = Solution()
inverted_tree = sol.invertTree(test_case.root)
if not inverted_tree:
    print([])
else:
    print(inverted_tree.convert_to_list())


