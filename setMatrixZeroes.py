# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # Find all zeroes
        zeroRows, zeroCols = set(), set()
        for rowIndex, row in enumerate(matrix):
            for colIndex, val in enumerate(row):
                if val == 0:
                    zeroRows.add(rowIndex)
                    zeroCols.add(colIndex)

        # Set rows to zero
        for row in zeroRows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0

        # Set cols to zero
        for col in zeroCols:
            for row in range(len(matrix)):
                matrix[row][col] = 0

