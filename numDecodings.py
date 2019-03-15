# A message containing letters from A-Z is being encoded to numbers using the following mapping:
# A - 1
# B - 2
# ...
# Z - 26
# Given a nonempty string containing only digits, 
# determine the total number of ways to decode it.
class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        if len(s) == 0:
            return 0
        
        res = [0] * (len(s) + 1)
        res[0] = 1
        for index in range(1, len(s) + 1):
            if s[index - 1] != '0':
                res[index] += res[index - 1]
            if index != 1 and s[index - 2: index] < '27' and s[index - 2:index] > '09':
                res[index] += res[index - 2]
                
        return res[-1]
