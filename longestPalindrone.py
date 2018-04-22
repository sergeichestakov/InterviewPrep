# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
        for index in range(len(s)):
            res = self.find_longest(s, index, index) #Odd Case
            if len(res) > len(longest):
                longest = res
            res = self.find_longest(s, index, index + 1) #Even Case
            if len(res) > len(longest):
                longest = res
        return longest

    #Expand out while still palindrone
    def find_longest(self, s, i1, i2):
        while i1 >= 0 and i2 < len(s) and s[i1] == s[i2]:
            i1 -= 1
            i2 += 1
        return s[i1 + 1: i2]

