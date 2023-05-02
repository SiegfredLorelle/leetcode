"""Remove Nth Node From End of List

Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
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
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ Solution using two pointers (O(1) memory) """
        # Initialize two pointers
        dummy = ListNode(next=head)
        start = dummy
        end = head

        # Move end pointer until there is a 'n' gap between start and end
        for _ in range(n):
            end = end.next

        # Move both pointers until end is at the end of the list (null)
        while end:
            start = start.next
            end = end.next
        
        # Delete the node in front of start node
        start.next = start.next.next
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
linked_list = LinkedList([1,2,3,4,5])
n = 2

sol = Solution()
new_linked_list = sol.removeNthFromEnd(linked_list.head_node, n)
if new_linked_list:
    result = new_linked_list.print_linked_list()
    print(result)
else:
    print([])