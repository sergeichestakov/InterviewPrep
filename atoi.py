# Implements atoi which converts a string into an integer
# Discards all white space characters until non white space is found, then takes an optional '+' or '-' depending on the sign
# Discards all characters after the number or exits if first non white space characters are not valid integers
# Converts to Max int or Min int if result is out of bounds for 32-bit integers
# Returns 0 if no valid conversion is performed

class Solution:
   MAX_INT = 2147483647
   def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        negative = False
        processing = False
        digits = []
        for char in str:
            if char == ' ': #Consume initial white space or break if encountered after number
                if processing:
                    break
                else:
                    continue
            elif char == '-' or char == '+': #Begin processing
                if processing:
                    break
                else:
                    if char == '-': #Negate
                        negative = True
                    processing = True
            else: #Try to convert character to number and add to digits
                processing = True
                try:
                    num = int(char)
                except: #Not a number
                    break
                digits.append(num)

        power = len(digits) - 1
        for digit in digits: #Create final number by iterating through digits
            result += digit * 10**power
            power -= 1

        if result > Solution.MAX_INT: #Check for overflow
            result = Solution.MAX_INT + 1 if negative else Solution.MAX_INT

        if negative:
            result = -result

        return result

