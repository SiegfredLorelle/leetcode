"""Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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


from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], 
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create dummy node to avoid edge cases (adding to an empty node)
        dummy = ListNode()
        current = dummy

        # Find the lower node between the two linked lists
        # Start from the head and move onwards
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        # Append the rest of the node(s) of the non-empty linked list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next



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
linked_list1 = LinkedList([1,2,4])
linked_list2 = LinkedList([1,3,4])

sol = Solution()
reversed_linked_list = sol.mergeTwoLists(linked_list1.head_node, 
                                         linked_list2.head_node)
if reversed_linked_list:
    result = reversed_linked_list.print_linked_list()
    print(result)
else:
    print([])