# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

class Solution:
    
    def longestValidParentheses(self, s: 'str') -> 'int':
        longest = 0
        stack = []
        
        stack.append(-1)
        for index, char in enumerate(s):
            if char == '(': # Add to stack and continue
                stack.append(index)
            elif char == ')': # Find longest by comparing to value in stack
                stack.pop() 
                if not stack:
                    stack.append(index)
                else:
                    longest = max(longest, index - stack[-1])
                
        return longest
