# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if row and row[-1] >= target:
                return self.binarySearch(row, target)

        return False

    def binarySearch(self, arr, val):
        low, high = 0, len(arr) - 1
        found = False
        while low <= high and not found:
            mid = low + (high - low) // 2
            if arr[mid] == val:
                found = True
            elif arr[mid] > val:
                high = mid - 1
            else:
                low = mid + 1

        return found
