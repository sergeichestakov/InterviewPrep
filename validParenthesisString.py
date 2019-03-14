# Given a string containing only three types of characters: '(', ')' and '*', 
# write a function to check whether this string is valid. 
# We define the validity of a string by these rules:
# - Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# - Any right parenthesis ')' must have a corresponding left parenthesis '('.
# - Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# - '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# - An empty string is also valid.
class Solution:
    def checkValidString(self, s: str) -> bool:
        maxOpen = minOpen = 0
        
        for char in s:
            if char == '(':
                maxOpen += 1
                minOpen += 1
            elif char == ')':
                maxOpen -= 1
                minOpen = max(minOpen - 1, 0)
            elif char == '*':
                maxOpen += 1
                minOpen = max(minOpen - 1, 0)
            
            if maxOpen < 0:
                return False
        
        return minOpen == 0
