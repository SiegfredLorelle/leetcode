"""Reverse Linked List

Given the head of a singly linked list, reverse the list, 
and return the reversed list.
"""

from typing import Optional

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


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """Solution using iteration"""
        current_node = head
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        return prev_node
        
        """Solution using recursion"""
        # if not head:
        #     return None

        # next_node = head
        # if head.next:
        #     next_node = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None
        
        # return next_node





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
test_case = LinkedList([1,2,3,4,5])

sol = Solution()
reversed_linked_list = sol.reverseList(test_case.head_node)
if reversed_linked_list:
    result = reversed_linked_list.print_linked_list()
    print(result)
else:
    print([])