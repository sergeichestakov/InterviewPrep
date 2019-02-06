# Given two binary strings, return their sum (also a binary string).
# The input strings are both non-empty and contains only characters 1 or 0.
class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        longest, shortest = (a, b) if len(a) >= len(b) else (b, a)
        ZERO, ONE = "0", "1"
        
        ans = ""
        carry = False
        for index in range(len(shortest)): # Add common parts
            x = longest[len(longest) - index - 1]
            y = shortest[len(shortest) - index - 1]
            if x == ONE and y == ONE:
                if carry:
                    ans += ONE
                else:
                    ans += ZERO
                    carry = True
            elif x == ONE or y == ONE:
                if carry:
                    ans += ZERO
                else:
                    ans += ONE
            else: # Both zero
                if carry:
                    ans += ONE
                    carry = False
                else:
                    ans += ZERO
                    
        diff = len(longest) - len(shortest)
        for index in range(diff): # Compare the rest if there is more
            char = longest[diff - index - 1]
            if char == ZERO:
                if carry:
                    ans += ONE
                    carry = False
                else:
                    ans += ZERO
                    
            elif char == ONE:
                if carry:
                    ans += ZERO
                else:
                    ans += ONE
        
        if carry: # Add extra digit 
            ans += ONE
            
        return ans[::-1]
