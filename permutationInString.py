#Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
#In other words, one of the first string's permutations is the substring of the second string.

class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #Check that each window of len(s1) has each letter of s1 exactly once -> return true
        s1Vals = [ord(char) - ord('a') for char in s1]
        s2Vals = [ord(char) - ord('a') for char in s2]

        target = [0] * 26
        for val in s1Vals: #Keep track of how many of each letter there were in original string
            target[val] += 1

        window = [0] * 26
        sLen = len(s1)

        for index in range(len(s2)): #Mark each letter you've seen thus far
            currLetter = s2Vals[index]
            window[currLetter] += 1
            if index >= sLen: #Delete char outside window
                prevLetter = s2Vals[index - sLen]
                window[prevLetter] -= 1
            if target == window: #Same amount of letters
                return True

        return False #Not found
