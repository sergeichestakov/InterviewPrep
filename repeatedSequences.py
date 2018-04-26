# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        strSet = set()
        ret = []
        n = len(s) - 9
        for index in range(n):
            subStr = s[index:index + 10]
            if subStr in strSet and subStr not in ret: #Weve seen it before but havent added it
                ret.append(subStr)
            strSet.add(subStr)

        return ret
