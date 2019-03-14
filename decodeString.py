# Given an encoded string, return it's decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the 
# square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, 
# square brackets are well-formed, etc.
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        stack.append(['', 1]) # Stack contains ('current string', multiplier)
        num = ''
        for char in s:
            if char.isdigit():
                num += char
            elif char == '[':
                stack.append(['', int(num)])
                num = ''
            elif char == ']':
                string, k = stack.pop()
                stack[-1][0] += string * k
            else:
                stack[-1][0] += char
                
        return stack[0][0]
