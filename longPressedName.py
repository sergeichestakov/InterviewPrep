# Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.
# You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        curr = 0
        for char in name:
            if curr == len(typed):
                return False
           
            # There is a mismatch
            if typed[curr] != char:
                if curr == 0 or typed[curr - 1] != typed[curr]:
                    return False
               
                # Discard similar chars
                prevChar = typed[curr]
                while curr < len(typed) and typed[curr] == prevChar:
                    curr += 1
                   
                # Next isnt a match
                if curr == len(typed) or typed[curr] != char:
                    return False
                
            curr += 1
            
        return True
