# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.
class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        if n == 1:
            return 1
        
        res = [0] * n
        res[0], res[1] = 1, 2
        for index in range(2, n):
            res[index] = res[index - 1] + res[index - 2]
            
        return res[-1]
