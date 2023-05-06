"""Merge k Sorted Lists

You are given an array of k linked-lists lists, 
each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None


        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None

                merged_list.append(self.mergeList(list1, list2))
                
            lists = merged_list

        return lists[0]


    def mergeList(self, list1, list2):
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next


        if list1:
            current.next = list1
        if list2:
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

linked_lists  = [
    LinkedList([1,3,4]).head_node1,
    LinkedList([2,6]).head_node,
    LinkedList([1,4,5]).head_node,
]

sol = Solution()
reversed_linked_list = sol.mergeKLists(linked_lists)
if reversed_linked_list:
    result = reversed_linked_list.print_linked_list()
    print(result)
else:
    print([])