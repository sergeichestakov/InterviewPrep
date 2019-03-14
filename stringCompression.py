# Given an array of characters, compress it in-place.
# The length after compression must always be smaller than or equal to the original array.
# Every element of the array should be a character (not int) of length 1.
# After you are done modifying the input array in-place, return the new length of the array.
class Solution:
    def compress(self, chars: List[str]) -> int:
        currChar = chars[0]
        count = 0
        ret = []
        for char in chars:
            if char == currChar:
                count += 1
            else:
                ret.append(currChar)
                if count != 1:
                    ret.extend([char for char in str(count)])
                currChar = char
                count = 1
        
        ret.append(currChar)
        if count != 1:
            ret.extend([char for char in str(count)])
                
        for index in range(len(ret)):
            chars[index] = ret[index]
        return len(ret)
