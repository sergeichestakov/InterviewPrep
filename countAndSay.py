#The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n, generate the nth term of the count-and-say sequence.

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ret = "1"
        term = 1

        # Generate string for each term
        while term < n:
            newStr = ""
            prevChar = ret[0]
            count = 1
            # Count number of occurrences for each char
            for index in range(1, len(ret)):
                char = ret[index]
                if char == prevChar:
                    count += 1
                else: # Different character so append occurrences and number
                    newStr += str(count) + str(prevChar)
                    prevChar = char
                    count = 1

            # Save previous string and advance to next term
            newStr += str(count) + str(prevChar)
            ret = newStr
            term += 1

        return ret
