"""LRU Cache

Design a data structure that follows the constraints 
of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, 
    otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. 
    Otherwise, add the key-value pair to the cache. 
    If the number of keys exceeds the capacity from this operation, 
    evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.
"""
import collections

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:
    """ SOLUTION USING BUILT IN DATA STRUCTURE (ORDERD DICT) """
    # def __init__(self, capacity: int):
    #     self.cache = collections.OrderedDict([])
    #     self.capacity = capacity

    # def get(self, key: int) -> int:
    #     if key in self.cache:
    #         self.cache.move_to_end(key)
    #         return self.cache[key]
    #     return -1

    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache:
    #         self.cache.move_to_end(key)
    #     self.cache[key] = value

    #     if len(self.cache) > self.capacity:
    #         self.cache.popitem(last=False)

    """ SOLUTION USING DOUBLY LINKED LIST """
    def __init__(self, capacity: int):
        self.cache = {} # key : node
        self.capacity = capacity

        # Use for finding the least recent key and most recent key
        self.least, self.recent = Node(0, 0), Node(0, 0) 
        self.least.next, self.recent.prev = self.recent, self.least
        

    def remove(self, node):
        """Remove the given node from the linked list"""
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev

    def add(self, node):
        """Add a node to the right of the linked list"""
        prev, nxt = self.recent.prev, self.recent
        prev.next = nxt.prev = node
        self.recent.prev = node
        node.next = nxt
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            # Move the node to the front
            self.remove(self.cache[key])
            self.add(self.cache[key])

            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update the value 
            # then move the node to the front
            self.remove(self.cache[key])
        
        # Add the new keys and values in linked list and cache
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        # Remove the least used key if over the capacity
        if len(self.cache) > self.capacity:
            lru = self.least.next
            self.remove(lru)
            self.cache.pop(lru.key)



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
cmds = ["put","put","get","put","get","put","get","get","get"]
params = [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

# print(cmds, params)
res = [None]
for cmd, param in zip(cmds, params):
    param = tuple(param)
    res.append(eval(f"obj.{cmd}{param}"))

print(res)