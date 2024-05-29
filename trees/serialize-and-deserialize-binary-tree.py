"""Serialize and Deserialize Binary Tree
Serialization is the process of converting a data structure or object 
into a sequence of bits so that it can be stored in 
a file or memory buffer, or transmitted across a network connection link 
to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm 
should work. 
You just need to ensure that a binary tree can be serialized 
to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as 
how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.serializedString = ""

        def dfs(node):
            if not node:
                self.serializedString += "E,"
                return
            else:
                self.serializedString += f"{node.val},"

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.serializedString

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        start = TreeNode("E")
        currNode = start
        toRight = False
        passed = []

        dataAsArr = data.split(",")
        for num in dataAsArr:
            if num == "E":
                if not passed:
                    break
                currNode = passed.pop()
                toRight = True
        
            else:
                newNode = TreeNode(num)
                if not toRight:
                    currNode.left = newNode
                else:
                    currNode.right = newNode
                toRight = False
                currNode = newNode
                passed.append(currNode)


        return start.left


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))