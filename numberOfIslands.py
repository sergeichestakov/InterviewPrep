# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.
class Solution:
    def inBounds(self, row: 'int', col: 'int', grid: 'List[List[any]]'):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])
    
    def markSeen(self, grid: 'List[List[str]]', seen: 'List[List[bool]]', row: 'int', col: 'int'):
        seen[row][col] = True
        possible = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
        for newrow, newcol in possible:
            if self.inBounds(newrow, newcol, seen) and not seen[newrow][newcol] and grid[newrow][newcol] == '1':
                self.markSeen(grid, seen, newrow, newcol)
        
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        numIslands = 0
        seen = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for rowIndex, row in enumerate(grid):
            for colIndex, val in enumerate(row):
                if val == '1' and not seen[rowIndex][colIndex]:
                    numIslands += 1
                    self.markSeen(grid, seen, rowIndex, colIndex)
                    
        return numIslands
