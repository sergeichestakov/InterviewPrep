# A robot is located at the top-left corner of a m x n grid.
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
# How many possible unique paths are there?
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.findPaths(m, n, {})

    def findPaths(self, m, n, paths):
        if m == 1 or n == 1: # Base case: can only move in 1 direction
            return 1

        # Memoize as sorted tuple because 5x3 has same solution as 3x5
        coords = tuple(sorted((m, n)))
        if coords not in paths: # Sum moving down and to the right
            paths[coords] = self.findPaths(m - 1, n, paths) + self.findPaths(m, n - 1, paths)

        return paths[coords]
