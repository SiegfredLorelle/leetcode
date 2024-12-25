"""Task Scheduler
You are given an array of CPU tasks, 
each labeled with a letter from A to Z, and a number n. 
Each CPU interval can be idle or allow the completion of one task. 
Tasks can be completed in any order, 
but there's a constraint: there has to be a gap of at least n intervals 
between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.
"""

from typing import List
import heapq
import collections
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count fequencies of the same task
        taskCount = {}
        for task in tasks:
            taskCount[task] = taskCount.get(task, 0) + 1
        
        # Build max heap by negating task count
        maxHeap = [-taskCount[task] for task in taskCount]
        heapq.heapify(maxHeap)

        # Loop until all tasks have been processed
        queue = collections.deque([])
        time = 0
        while maxHeap or queue:
            time += 1
            # Process a task in heap, 
            # if no available task, skip time to the next available task
            if not maxHeap:
                time = queue[0][1]
            else:
                taskCount = heapq.heappop(maxHeap) + 1
                if taskCount:
                    queue.append((taskCount, time + n))

            # Add the task back if their cooldown has passed
            if queue and queue[0][1] <= time:
                taskCount, _ = queue.popleft()
                heapq.heappush(maxHeap, taskCount)
        return time