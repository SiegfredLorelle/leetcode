"""Course Schedule II
There are a total of numCourses courses you have to take, 
labeled from 0 to numCourses - 1. 
You are given an array prerequisites where 
prerequisites[i] = [ai, bi] indicates 
that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], 
indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. 
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.
"""

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        # Each course maps to a set of its prerequisites       
        adjList = {num: [] for num in range(numCourses)}
        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        # Used to detect cycles
        cycle = set()
        # Used to keep track of taken courses
        taken = set() 

        # DFS to detect cycles and determine course order
        def dfs(course):
            if course in taken:
                return True
            if course in cycle:
                return False

            cycle.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
                taken.add(prereq)

            cycle.discard(course)
            taken.add(course)
            res.append(course)
            return True

        # Process each course to ensure all can be completed
        for num in range(numCourses):
            if not dfs(num):
                return []

        return res