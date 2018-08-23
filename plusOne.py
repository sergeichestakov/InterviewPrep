# Given a non-empty array of digits representing a non-negative integer, add one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Add one to the end
        index = len(digits) - 1
        digits[index] += 1

        # Carry digits over as needed
        carry = digits[index] == 10
        while carry:
            # Reset and check bounds
            digits[index] = 0
            if index == 0:
                break
            # Move on to next place
            index -= 1
            digits[index] += 1
            carry = digits[index] == 10

        return digits if not carry else [1] + digits
