# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell, 
# where "adjacent" cells are those horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.
class Solution:
    def inBounds(self, row: 'int', col: 'int', board: 'List[List[str]]'):
        return row >=0 and row < len(board) and col >= 0 and col < len(board[0])
    
    def search(self, board: 'List[List[str]]', seen: 'List[List[bool]]', \
               rIndex: 'int', cIndex: 'int', word: 'str') -> 'bool':

        if not word: # Empty string
            return True
        
        first = word[0]
        possible = [(rIndex + 1, cIndex), (rIndex - 1, cIndex), \
                    (rIndex, cIndex + 1), (rIndex, cIndex - 1)]
        for row, col in possible:
            if self.inBounds(row, col, board):
                if board[row][col] == first and not seen[row][col]:
                    seen[row][col] = True
                    if self.search(board, seen, row, col, word[1:]):
                        return True
                    seen[row][col] = False
                
        return False
        
    def exist(self, board: 'List[List[str]]', word: 'str') -> 'bool':
        seen = [[False for _ in range(len(board[0]))] for _ in range(len(board))] 
        
        first = word[0]
        for rIndex, row in enumerate(board):
            for cIndex, val in enumerate(row):
                if val == first:
                    seen[rIndex][cIndex] = True
                    if self.search(board, seen, rIndex, cIndex, word[1:]):
                        return True
                    seen[rIndex][cIndex] = False
                    
        return False
