# A zero-indexed array A of length N contains all integers from 0 to N-1.
# Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.
# Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]…
# By that analogy, we stop adding right before a duplicate element occurs in S.

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest, curr = 0, 0
        seen = [False] * len(nums)

        # Find longest cycle and stop when we encounter a visited index
        for index in range(len(nums)):
            while not seen[index]:
                seen[index] = True
                index = nums[index]
                curr += 1
            longest = max(longest, curr)
            curr = 0

        return longest

