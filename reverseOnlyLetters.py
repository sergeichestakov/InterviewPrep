# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        clist = list(S)
        front, end = 0, len(clist) - 1
        while front < end:
            while front < len(clist) and not clist[front].isalpha():
                front += 1
            while end >= 0 and not clist[end].isalpha():
                end -= 1
                
            if front < end:
                clist[front], clist[end] = clist[end], clist[front]
                
            front += 1
            end -= 1
                
        return ''.join(clist)
