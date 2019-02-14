# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':        
        maxArea = 0
        left, right = 0, len(height) - 1
        
        # Keep two pointers and find area of container at each step
        while(left < right):
            maxArea = max(maxArea, (right - left) * min(height[left], height[right]))
            if height[left] >= height[right]: # Move the smaller pointer
                right -= 1
            else:
                left += 1
        
        return maxArea
