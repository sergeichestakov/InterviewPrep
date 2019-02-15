# Given a query string and a text string, write a function 'highlight' 
# that returns the text with every occurance of the query wrapped in bold tags as such: "<b>query</b>"
# Multiple overlapping occurances should be contained within one set of bold tags.
def highlight(query, text):
    result = ""
    index = 0
    length = len(query)
    starting = [] # Find intervals of each occurance
    for index in range(len(text)):
        substr = text[index: index + length]
        if substr == query:
            starting.append([index, index + length])

    if not starting: # No occurances of query
        return text

    res = [starting[0]] # Remove overlapping intervals
    for next in starting[1:]:
        currstart, currend = res[-1]
        nextstart, nextend = next
        if nextstart <= currend:
            res[-1][1] = max(currend, nextend) # Update end position
        else:
            res.append(next)

    # Construct the string with bold tags
    prevStart = 0
    for start, end in res:
        result += text[prevStart:start] + '<b>' + text[start:end] + '</b>'
        prevStart = end

    result += text[prevStart:]
    return result
