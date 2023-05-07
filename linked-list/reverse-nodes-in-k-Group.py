"""Reverse Nodes in k-Group

Given the head of a linked list, 
reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and 
is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, 
in the end, should remain as it is.

You may not alter the values in the list's nodes, 
only nodes themselves may be changed.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        # This is only added to view the result of the solution
    def print_linked_list(self):
        """
        Convert a linked list into a python list
        starting from the given node.
        """
        new_list = [self.val]
        current_node = self.next
        while current_node:
            new_list.append(current_node.val)
            current_node = current_node.next
        return new_list


from typing import List, Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        prev_group = dummy
        k_node = dummy

        while True:
            # Move k node k times
            k_node = self.get_k_node(prev_group, k)
            if not k_node:
                return dummy.next
            next_group = k_node.next

            # Reverse the nodes within prev grp and next grp
            prev = k_node.next
            current = prev_group.next
            while current != next_group:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            # Connect the groups of nodes 
            nxt = prev_group.next 
            prev_group.next = k_node
            prev_group = nxt


    def get_k_node(self, current, k):
        """Returns the node after moving it k times"""
        while current and k > 0:
            current = current.next
            k -= 1
        return current



# Only purpose is to create a linked list from a python list for test cases
# This is not part of the solution
class LinkedList:
    def __init__(self, elements: list):
        if not elements:
            self.head_node = None
            return

        head_val = elements[0]
        self.head_node = ListNode(head_val, None)
        prev_node = self.head_node

        for element in elements[1 :]:
            new_node = ListNode(element, None)
            prev_node.next = new_node
            prev_node = new_node

# Change the values in the list here to try out other test cases

linked_list = LinkedList([1,2,3,4,5]).head_node

sol = Solution()
reversed_linked_list = sol.reverseKGroup(head=linked_list, k=2)
if reversed_linked_list:
    result = reversed_linked_list.print_linked_list()
    print(result)
else:
    print([])