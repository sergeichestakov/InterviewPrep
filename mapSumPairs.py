# Implement a MapSum class with insert, and sum methods.
# For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value.
# If the key already existed, then the original key-value pair will be overridden to the new one.
# For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.
# For this problem we will implement a prefix tree (trie)

class Node:
    def __init__(self, value=0):
        self.children = {}
        self.value = value

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        index_last_char = None
        for index_char, char in enumerate(key):
            if char in node.children:
                node = node.children[char]
            else:
                index_last_char = index_char
                break

        # append new nodes for the remaining characters, if any
        if index_last_char is not None:
            for char in key[index_last_char:]:
                node.children[char] = Node()
                node = node.children[char]

        # store value in the terminal node
        node.value = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for char in prefix: #Traverse
            if char not in node.children:
                return 0
            node = node.children[char]
        return self.getSum(node)

    def getSum(self, node):
        if node.children is None: #Leaf
            return node.value
        sum = node.value
        for child in node.children.values():
            sum += self.getSum(child)
        return sum

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
