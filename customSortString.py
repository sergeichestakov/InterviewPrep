# S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
# S was sorted in some custom order previously. We want to permute the characters of T so that they match the order that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.
# Return any permutation of T (as a string) that satisfies this property.
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        front = 0
        clist = list(T)
        for char in S:
            indices = [index for index, ltr in enumerate(clist) if ltr == char]
            
            for index in indices:
                clist[front], clist[index] = clist[index], clist[front]
                front += 1
                
        return ''.join(clist)
