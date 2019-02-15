# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
# The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
class Solution:
    def judgeCircle(self, moves: 'str') -> 'bool':
        pos = (0, 0)
        
        for move in moves:
            x, y = pos
            if move == "U":
                pos = (x, y + 1)
            elif move == "D":
                pos = (x, y - 1)
            elif move == "R":
                pos = (x + 1, y)
            elif move == "L":
                pos = (x - 1, y)
                
        return pos == (0, 0)
