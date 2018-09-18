# Given a roman numeral as a string, convert it to an integer.

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        value = 0
        for index in range(len(s) - 1):
            curr = Roman[s[index]]
            next = Roman[s[index + 1]]
            if next > curr: # Smaller number before larger implies substraction
                value -= curr
            else: # Add it to value
                value += curr

        return value + Roman[s[-1]]
