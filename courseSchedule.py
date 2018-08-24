# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# The prerequisites can be represented as a directed graph.
# The problem can then be interpreted as finding a cycle in such a graph which can be done using a modified form of DFS.
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Construct graph
        edges = {}
        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]
            if course not in edges:
                edges[course] = []
            edges[course].append(prereq)

        # Use DFS and keep track of back edges to find cycle
        visited = [False] * numCourses
        stack = [False] * numCourses
        for node in range(numCourses):
            if not visited[node]:
                if self.hasCycle(node, visited, stack, edges):
                    return False

        return True

    def hasCycle(self, node, visited, stack, edges):
        visited[node] = True
        stack[node] = True

        # Check all children
        if node in edges:
            for child in edges[node]:
                if stack[child]: # Encountered already so cycle detected
                    return True
                elif self.hasCycle(child, visited, stack, edges):
                    return True

        # Remove from stack and return
        stack[node] = False
        return False
