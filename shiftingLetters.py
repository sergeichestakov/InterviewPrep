# We have a string S of lowercase letters, and an integer array shifts.
# Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.
# Return the final string after all such shifts to S are applied.
class Solution:
    def shift(self, char: str, amount: int):
        value = ord(char)
        shifted = value + amount
        if shifted > ord('z'):
            shifted -= 26
        return chr(shifted)
        
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        clist = list(S)
        amounts = shifts[:]
        
        amounts[-1] %= 26
        for index in range(len(amounts) - 2, -1, -1):
            amounts[index] += amounts[index + 1]
            amounts[index] %= 26
         
        for index in range(len(amounts)):
            clist[index] = self.shift(clist[index], amounts[index])
            
        return ''.join(clist)
