# Given two words word1 and word2, find the minimum number of steps required to 
# make word1 and word2 the same, where in each step you can delete 
# one character in either string. 
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        table = [[0] * (n + 1) for _ in range(m + 1)]
 
	# Longest common subsequence       
        for row in range(m):
            for col in range(n):
                table[row + 1][col + 1] = max(table[row + 1][col], table[row][col + 1], \
                                              table[row][col] + (word1[row] == word2[col]))
        return m + n - 2 * table[m][n]
