"""Time Based Key-Value Store

Design a time-based key-value data structure 
that can store multiple values for the same key at different time stamps 
and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

- TimeMap() Initializes the object of the data structure.
- void set(String key, String value, int timestamp) Stores the key key 
    with the value value at the given time timestamp.
- String get(String key, int timestamp) 
    Returns a value such that set was called previously, 
    with timestamp_prev <= timestamp. If there are multiple such values, 
    it returns the value associated with the largest timestamp_prev. 
    If there are no values, it returns "".
"""

class TimeMap:

    def __init__(self):
        self.timemap = {} # key : {timestamp : value}
        self.timestamps = {} # key : [timestamps]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Create an empty list & dict if this is the first one
        if key not in self.timemap:
            self.timemap[key] = {}
            self.timestamps[key] = []
        # Set the value to the appropriate key and timestamp
        self.timemap[key][timestamp] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        # Ensure that the key exists
        if key not in self.timemap:
            return ""

        # Return the value if the given key and timestamp have a match
        if self.timemap[key].get(timestamp):
            return self.timemap[key][timestamp]
        
        # Ensure that given timestamp has a valid value 
        # (Must have an earlier timestamp with a value)
        lowest_timestamp = self.timestamps[key][0] 
        if timestamp < lowest_timestamp:  
            return ""

        # Use binary search to find the closest lower bound timestamp 
        start = 0
        end = len(self.timestamps[key]) - 1
        while start <= end:
            middle = (start + end) // 2
            if self.timestamps[key][middle] < timestamp:
                start = middle + 1
            else:
                end = middle - 1

        return self.timemap[key][self.timestamps[key][end]]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)



obj = TimeMap()
cmds = ["set","get","get","set","get","get"]
params = [
    ["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]
]

# print(cmds, params)
res = [None]
for cmd, param in zip(cmds, params):
    param = tuple(param)
    res.append(eval(f"obj.{cmd}{param}"))

print(res)