# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
class Solution:
    nextState = {
        "RIGHT": "DOWN",
        "DOWN": "LEFT",
        "LEFT": "UP",
        "UP": "RIGHT"
    }

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        res = []

        # Construct visited matrix
        visited = [[False for col in range(len(matrix[0]))] for row in range(len(matrix))]

        currRow, currCol = 0, 0

        currState = "RIGHT"
        while currState != "DONE": # Append to array, mark visited, and advance index
            res.append(matrix[currRow][currCol])
            visited[currRow][currCol] = True
            currRow, currCol, currState = self.advance(currRow, currCol, currState, matrix, visited)

        return res

    def advance(self, currRow, currCol, state, matrix, visited):
        oldState = state

        while True:
            # Increment according to state
            row, col = currRow, currCol
            if state == "RIGHT":
                col += 1
            elif state == "DOWN":
                row += 1
            elif state == "LEFT":
                col -= 1
            elif state == "UP":
                row -= 1

            # Check index
            if self.inBounds(row, col, matrix) and not visited[row][col]:
                return row, col, state
            else: # If invalid index, recalculate state and try again
                state = self.nextState[state]
                if state == oldState: # Back to where we started so we're done
                    return 0, 0, "DONE"

    def inBounds(self, row, col, matrix):
        return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])

