# Returns whether an integer is a palindrome (can be read the same forward and backward)
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        strNum = str(x)
        return self.checkPalindrone(strNum)

    def checkPalindrome(self, strNum):
        length = len(strNum)
        if length == 1:
            return True
        elif length == 2:
            return strNum[0] == strNum[1]
        else:
            return strNum[0] == strNum[-1] and self.checkPalindrone(strNum[1:-1])

