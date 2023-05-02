"""Linked List Cycle

Given head, the head of a linked list, 
determine if the linked list has a cycle in it.

There is a cycle in a linked list 
if there is some node in the list 
that can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node 
that tail's next pointer is connected to. 
Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

# Definition for singly-linked list.
class ListNode:
    # The next pointer is for testing only
    def __init__(self, x, next):
        self.val = x
        self.next = None


from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        """Solution using hashmaps ((n) memory)"""
        # visited = set()

        # # Check if the node is already visited
        # current = head
        # while current:
        #     if current in visited:
        #         return True

        #     visited.add(current)
        #     current = current.next

        # return False

        
        # """Solution using two pointers (O(1) memory)"""
        slow, fast =1


class LinkedList:
    def __init__(self, elements: list, pos: int):
        if not elements:
            self.head_node = None
            return

        nodes = []
        head_val = elements[0]
        self.head_node = ListNode(head_val, None)
        prev_node = self.head_node
        nodes.append(self.head_node)

        for element in elements[1 :]:
            new_node = ListNode(element, None)
            prev_node.next = new_node
            prev_node = new_node
            nodes.append(new_node)
        
        if pos >= 0:
            nodes[-1].next = nodes[pos]

# Change the values in the list here to try out other test cases
linked_list = LinkedList([3,2,0,4], 1)

sol = Solution()
result = sol.hasCycle(linked_list.head_node)
print(result)