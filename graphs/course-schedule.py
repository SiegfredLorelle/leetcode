"""Course Schedule
There are a total of numCourses courses you have to take, 
labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] 
indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], 
indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Each course maps to a set of its prerequisites       
        adjList = {num: set() for num in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].add(prereq)

        # DFS to check for cycles in the prerequisite graph
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if not adjList[course]:
                return True

            visited.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            adjList[course].clear()
            visited.remove(course)
            return True

        # Check each course to ensure all can be completed
        for num in range(numCourses):
            if not dfs(num):
                return False
        return True