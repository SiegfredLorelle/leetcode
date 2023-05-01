"""Add Two Numbers

You are given two non-empty linked lists 
representing two non-negative integers. 
The digits are stored in reverse order, 
and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            # Check for edge case where one list is already empty
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            # # Compute value
            total = l1_val + l2_val + carry
            carry = total // 10
            node_val = total % 10
            current.next = ListNode(node_val)
            # # Or use str to get the values by index
            # total = str(l1_val + l2_val + carry)
            # carry = 0
            # if len(total) > 1:
            #     carry = int(total[0])
            # current.next = ListNode(int(total[-1]))
            
            # Update pointers
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

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
linked_list1 = LinkedList([9,9,9,9,9,9,9])
linked_list2 = LinkedList([9,9,9,9])

sol = Solution()
reordered_linked_list = sol.addTwoNumbers(
    linked_list1.head_node, 
    linked_list2.head_node
    )

if reordered_linked_list:
    result = reordered_linked_list.print_linked_list()
    print(result)
else:
    print([])