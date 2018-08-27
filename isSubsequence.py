class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return False

        indices = {}
        # Store each index of every char
        for index, char in enumerate(t):
            if char not in indices:
                indices[char] = []
            indices[char].append(index)

        # Check to make sure there exists an index for each letter
        # that is strictly greater than one for the previous
        prevIndex = -1
        for index, char in enumerate(s):
            if char not in indices: # This letter is not in t
                return False
            found = False
            for numAppearance, charIndex in enumerate(indices[char]):
                if charIndex > prevIndex: # Found valid index
                    indices[char] = indices[char][numAppearance + 1:] # Cut array short to speed up future checks
                    prevIndex = charIndex
                    found = True
                    break
            if not found:
                return False

        return True

    # Faster solution with O(1) space
    def betterSolution(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        sIndex, tIndex = 0, 0

        # Compare chars in order and advance indices accordingly
        while sIndex < len(s) and tIndex < len(t):
            if s[sIndex] == t[tIndex]:
                sIndex += 1
            tIndex += 1

        return sIndex == len(s)
