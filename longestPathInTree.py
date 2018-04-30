# Consider an undirected tree with N nodes, numbered from 1 to N. Each node has a label associated with it, which is an integer value.
# Given an array A of length N, where A[j] is the label value of the (j + 1) node in the tree and array E of length K = (n - 1) * 2 in which the edges of the tree are described.
# Return the length of the longest path such that all the nodes on that path have the same label.
def solution(A, E):
    edges = {}
    for index in range(0, len(E), 2): #fill out edges dict to easily find children of a node
        node = E[index]
        child = E[index + 1]
        if node not in edges:
            edges[node] = []

        edges[node].append(child)

    longest = 0
    checked = set() #Fill out in checkChild so we dont check the same node twice
    for index in range(len(A)):
        node = index + 1
        #Check that children have same value
        if node not in checked:
            count = checkChild(node, A, edges, checked)
            longest = max(longest, count)

    return longest

#Returns count of same value
def checkChild(node, A, edges, checked):
    checked.add(node)
    value = A[node - 1]
    count = 0

    if node not in edges: #reached a leaf so stop checking
        return 0
    for child in edges[node]: #Check all children and recurse
        childValue = A[child - 1]
        if childValue == value:
            count = count + checkChild(child, A, edges, checked) + 1

    return count
