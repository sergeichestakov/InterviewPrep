# Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
# Return the maximum valued number you could get.
class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        # Check each digit starting from the left to find the largest digit in the number that can replace it.
        # If there is a larger digit, select the SMALLEST index of the LARGEST digit
        # Move on if it does not exist

        numStr = str(num)
        indices = {} # Stores smallest index of each number
        for index, digit in enumerate(numStr):
            indices[int(digit)] = index

        for index, digit in enumerate(numStr):
            for d in range (9, int(digit), -1): # Find largest number that can replace it
                if d in indices and indices[d] > index: # Must be in the number and a smaller power (higher index)
                    # Swap and return result
                    newIndex = indices[d]

                    newStr = list(numStr)
                    newStr[newIndex], newStr[index] = newStr[index], newStr[newIndex]
                    return int(''.join(newStr))

        return num
