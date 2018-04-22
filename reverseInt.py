# Given a 32-bit signed integer, reverse digits of an integer.
# Return 0 on overflow
class Solution:
    MAX_INT = 2147483648
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = True if x < 0 else False
        x = abs(x)
        power = len(str(x)) - 1 #Number of digits - 1
        result = 0
        while x > 0:
            digit = x % 10 #Extract digit, multiply by new power, and add to result
            result += digit * 10**power
            power -= 1
            x //= 10 #Integer division discards remainder

        if negative: #Negate
            result = -result

        #Check for overflow and return
        if result >= Solution.MAX_INT or result < -Solution.MAX_INT:
            return 0

        return result
