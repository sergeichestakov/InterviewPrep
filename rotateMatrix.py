#Rotate an n x n 2D matrix by 90 degrees (clockwise)
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        n = length - 1
        if n < 1: #Edge case of 1x1 or 0x0
            return

        offSet = 0
	#Algorithm runs for half the rows in the matrix and 2 fewer columns after every new row, hence the offset
        for row in range(length // 2):
            for col in range(offSet, length - offSet - 1):
                #col = n - row
                #row = col
                currElem = matrix[row][col]
                newRow = col
                newCol = n - row
                #Go around the matrix and replace until back to where we started
                while newRow != row or newCol != col:
                    replaceElem = matrix[newRow][newCol] #Save the element you are replacing
                    matrix[newRow][newCol] = currElem
                    currElem = replaceElem
                    prevRow = newRow #Calculate next position
                    newRow = newCol
                    newCol = n - prevRow

                matrix[row][col] = currElem
            offSet += 1
