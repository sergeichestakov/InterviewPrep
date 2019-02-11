# Returns whether or not a given string is a valid IPv4 address.
def isValid(ip):
    arr = ip.split('.')
    if len(arr) != 4:
        return False

    for num in arr:
        if len(num) == 0:
            return False
        
        if len(num) > 1 and num[0] == '0':
            return False
        try:        
            value = int(num)
        except ValueError:
            return False

        if value < 0 or value > 255:
            return False

    return True

# Returns whether or not you can convert a given string into a valid IP address
def canConvert(IPstr):
    length = len(IPstr)

    if length < 4 or length > 12:
        return False

    newStr = IPstr
   
    # Generate all possible IP addresses from a given string
    for first in range(1, length - 2):
        for second in range(first + 1, length - 1):
            for third in range(second + 1, length):
                newStr = newStr[:third] + '.' + newStr[third:]
                newStr = newStr[:second] + '.' + newStr[second:]
                newStr = newStr[:first] + '.' + newStr[first:]

                if isValid(newStr):
                    return True

                newStr = IPstr

    return False
