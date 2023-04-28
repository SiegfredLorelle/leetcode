"""Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. 
Only nodes themselves may be changed.
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        """Solution using an array (easier to implement but O(n) Memory)"""
        # # Definition for singly-linked list.
        # current = head
        # nodes = []
        # while current:
        #     nodes.append(current)
        #     current = current.next

        # i = 0
        # current = head
        # while nodes:
        #     if i % 2 == 0:
        #         current.next = nodes.pop(0)
        #     else:
        #         current.next = nodes.pop()
        #     current = current.next
        #     i += 1

        # current.next = None

        

        """Solution without using an array (O(1) Memory)"""
        # Determine the middle of the list    
        slow, fast = head, head.next
        current = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        # Reverse the 2nd half of the list
        current = slow.next
        prev = slow.next = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Merge the two halves
        first, second = head, prev
        while second:
            next_first, next_second = first.next, second.next
            first.next = second
            second.next = next_first
            first, second = next_first, next_second


        # This is added here but not on the Leetcode solution
        return head


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
linked_list = LinkedList([1,2,3,4,5])

sol = Solution()
reordered_linked_list = sol.reorderList(linked_list.head_node)
if reordered_linked_list:
    result = reordered_linked_list.print_linked_list()
    print(result)
else:
    print([])