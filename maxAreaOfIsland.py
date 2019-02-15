# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.
# Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
class Solution:
    def inBounds(self, row: 'int', col: 'int', grid: 'List[List[any]]'):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
    
    def findArea(self, grid: 'List[List[int]]', seen: 'List[List[bool]]', row: 'int', col: 'int'):
        area = 1
        seen[row][col] = True
        possible = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        for newrow, newcol in possible:
            if self.inBounds(newrow, newcol, seen) and not seen[newrow][newcol] and grid[newrow][newcol] == 1:
                area += self.findArea(grid, seen, newrow, newcol)
            
        return area
                
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':
        maxArea = 0
        seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for rowIndex, row in enumerate(grid):
            for colIndex, val in enumerate(row):
                if val == 1 and not seen[rowIndex][colIndex]:
                    area = self.findArea(grid, seen, rowIndex, colIndex)
                    maxArea = max(maxArea, area)
                    
        return maxArea
