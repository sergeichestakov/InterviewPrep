# Given a string A consisting of n characters and a string B consisting of m characters
# Write a function that will return the number of times A must be repeated such that B is a substring of A, or -1 if it cannot
def solution(A, B):
    N = len(A)
    M = len(B)
    count = 0
    startIndex = 0
    #Find the first instance of repeat
    for index in range(N):
        subStr = B[index: index + N] #Check each substring
        if subStr == A: #Found first repeat check until the end
            count += 1
            startIndex = index #Save start location
            newIndex = index
            while newIndex + N < M: #Check each full substr
                subStr = B[newIndex: newIndex + N]
                if subStr == A:
                    count += 1
                else:
                    return -1 #not a substring so return
                newIndex += N
            endIndex = startIndex #Save end location
            break

    firstChars = B[:startIndex] #Check beginning and end of string
    if firstChars in A and len(firstChars) > 0:
        count +=1
    endChars = B[endIndex:]
    if endChars in A and len(endChars) > 0:
        count += 1
    return count
