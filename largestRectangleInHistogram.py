# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxArea = 0
        stack = []

        #Iterate through the heights if > prevheight add to stack, if less pop off stack
        for time, height in enumerate(heights):
            if not stack or height > stack[-1][1]:
                stack.append((time, height))
                continue
            elif height < stack[-1][1]:
                while stack and height < stack[-1][1]: #Keep popping off the stack and comparing
                    prevTime, prevHeight = stack.pop()
                    #Area of the rectangle is height * time its been in the stack
                    area = prevHeight * (time - prevTime)
                    maxArea = max(area, maxArea)
                stack.append((prevTime, height))

        time = len(heights)
        #Empty out the stack
        while stack:
            prevTime, prevHeight = stack.pop()
            area = prevHeight * (time - prevTime)
            maxArea = max(area, maxArea)

        return maxArea
