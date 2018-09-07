'''
There is a rabbit that starts in the middle of an n x m matrix, n > 0, m > 0.
Each element of a matrix is an integer representing points gained for being on the spot.
If there are multiple possible "middles" then choose the one which has the highest point value to start on.
On each iteration, the rabbit can move up, left, right, or down.
The rabbit will always move to the next spot with the highest point value
and will "consume" those points (set the point value in that position to 0).
The rabbit spots when all positions around it are 0s. Calculate how many points the rabbit will score for a given m x n matrix.
'''

def getStartingPos(matrix):
    '''
    Returns the starting position and amount eaten at that point depending on matrix dimensions.
    '''
    halfRow, halfCol = len(matrix) // 2, len(matrix[0]) // 2
    rows = [halfRow] if len(matrix) % 2 else [halfRow, halfRow - 1]
    cols = [halfCol] if len(matrix[0]) % 2 else [halfCol, halfCol - 1]

    # Find maximum value of possible middles
    maxRow, maxCol = rows[0], cols[0]
    for row in rows:
        for col in cols:
            if matrix[row][col] > matrix[maxRow][maxCol]:
                maxRow, maxCol = row, col

    # Eat the middle and return initial conditions
    eaten = matrix[maxRow][maxCol]
    matrix[maxRow][maxCol] = 0
    return maxRow, maxCol, eaten

def getNextMoves(row, col, matrix):
    '''
    Finds all in bound and nonzero adjacent indices from a given position.
    Returns an array of tuples.
    '''
    possible = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
    nextMoves = []
    for newRow, newCol in possible: # Append all valid indices to return array
        if validIndex(newRow, newCol, matrix):
            nextMoves.append((newRow, newCol))

    return nextMoves

def validIndex(row, col, matrix):
    '''
    Returns if a given position is inbounds and nonzero (not visited)
    '''
    return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0]) and matrix[row][col]

def amountEaten(matrix):
    '''
    Returns the amount the rabbit will eat in a given matrix according to the rules above.
    '''
    row, col, eaten = getStartingPos(matrix)

    nextMoves = getNextMoves(row, col, matrix)
    while nextMoves: # Valid adjacent moves remain
        maxMove = 0
        for newRow, newCol in nextMoves: # Find max move
            if matrix[newRow][newCol] > maxMove:
                row, col, maxMove = newRow, newCol, matrix[newRow][newCol]

        # Eat max of adjacent, set to zero, and determine next moves from there
        eaten += matrix[row][col]
        matrix[row][col] = 0
        nextMoves = getNextMoves(row, col, matrix)

    return eaten

if __name__ == '__main__':
    mat = [[5, 7, 8, 6, 3],
           [0, 0, 7, 0, 4],
           [4, 6, 3, 4, 9],
           [3, 1, 0, 5, 8]]
    print(amountEaten(mat)) # Outputs 27
