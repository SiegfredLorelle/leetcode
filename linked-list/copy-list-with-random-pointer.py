"""Copy List with Random Pointer

A linked list of length n is given 
such that each node contains an additional random pointer, 
which could point to any node in the list, or null.

Construct a deep copy of the list. 
The deep copy should consist of exactly n brand new nodes, 
where each new node has its value 
set to the value of its corresponding original node. 
Both the next and random pointer of the new nodes 
should point to new nodes in the copied list 
such that the pointers in the original list and copied list 
represent the same list state. 
None of the pointers in the new list 
should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, 
where X.random --> Y, then for the corresponding two nodes x and y 
in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) 
that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list. """



# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

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
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # If None : None is not in the hash, use get function to access
        # values via keys to prevent edge cases
        old_to_copy = {None : None}

        current = head
        while current:
            old_to_copy[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            old_to_copy[current].next = old_to_copy[current.next]
            old_to_copy[current].random = old_to_copy[current.random]
            current = current.next

        return old_to_copy[head]
    



# Only purpose is to create a linked list from a python list for test cases
# This is not part of the solution
class LinkedList:
    def __init__(self, elements: list):
        if not elements:
            self.head_node = None
            return

        self.nodes = []

        head_val = elements[0][0]
        self.head_node = Node(head_val)
        prev_node = self.head_node
        self.nodes.append(self.head_node)

        for element in elements[1 :]:
            new_node = Node(element[0])
            prev_node.next = new_node
            prev_node = new_node
            self.nodes.append(new_node)

        for i, node in enumerate(self.nodes):
            if elements[i][1]:
                node.random = self.nodes[elements[i][1]]

# Change the values in the list here to try out other test cases
linked_list = LinkedList([[7,None],[13,0],[11,4],[10,2],[1,0]])

current_node = linked_list.head_node
while current_node:

    # print(current_node.val, current_node.next, current_node.random)
    current_node = current_node.next


# Note than index 0 is printed as None
sol = Solution()
new_linked_list = sol.copyRandomList(linked_list.head_node)
if new_linked_list:
    result = new_linked_list.print_linked_list()
    print(result)
else:
    print([])