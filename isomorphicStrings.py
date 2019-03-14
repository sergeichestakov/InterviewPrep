# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while 
# preserving the order of characters. No two characters may map to the 
# same character but a character may map to itself.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:        
        if len(s) != len(t):
            return False
    
        mapping = {}
        
        for index in range(len(s)):
            schar = s[index]
            tchar= t[index]
            
            if schar in mapping and mapping[schar] != tchar:
                return False
            
            mapping[schar] = tchar

            charSet = set()
            for key in mapping:
                if mapping[key] in charSet:
                    return False
                charSet.add(mapping[key])
            
        return True
