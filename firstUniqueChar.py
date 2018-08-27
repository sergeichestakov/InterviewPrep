#  Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()

        # Store indices of all nonrepeating characters
        nonRepeating = {}
        for index, char in enumerate(s):
            if char not in charSet:
                nonRepeating[char] = index
            elif char in nonRepeating:
                del nonRepeating[char]
            charSet.add(char)

        # None found so return -1
        if len(nonRepeating) == 0:
            return -1

        # Find the smallest index of nonrepeating characters
        smallestIndex = sys.maxsize
        for char in nonRepeating:
            smallestIndex = min(smallestIndex, nonRepeating[char])

        return smallestIndex
