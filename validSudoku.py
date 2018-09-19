# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()

        for rIndex, row in enumerate(board):
            for cIndex, val in enumerate(row):
                if val == '.': # Ignore unfilled space
                    continue
                # Generate possible combinations
                rowComb = ('row' + str(rIndex), val)
                colComb = ('col' + str(cIndex), val)
                squareComb = (rIndex // 3, cIndex // 3, val)
                # Check if we have seen them before
                if seen.intersection([rowComb, colComb, squareComb]):
                    return False
                # Add to set
                seen.update([rowComb, colComb, squareComb])

        return True
