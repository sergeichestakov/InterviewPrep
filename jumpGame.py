# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Determine if you are able to reach the last index.
class Solution:
    # Optimal solution O(n)
    def canJump(self, nums: 'List[int]') -> 'bool':
        lastPos = len(nums) - 1
        for index in range(len(nums) - 1, -1, -1):
            if index + nums[index] >= lastPos:
                lastPos = index
                
        return lastPos == 0
    
    # Original solution O(n^2). Timed out for one test case 
    def _canJump(self, nums: 'List[int]') -> 'bool':
        canReach = [False] * len(nums)
        canReach[0] = True
        
        for index, maxJump in enumerate(nums):
            if canReach[index]:
                for length in range(1, maxJump + 1):
                    if index + length >= len(nums):
                        return True
                    canReach[index + length] = True
                    
        return canReach[-1]
