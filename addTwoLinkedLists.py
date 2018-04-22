# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = False
        stack = []
        while(l1 and l2): #Add and push ListNodes onto the stack
            sum = l1.val + l2.val
            if carry:
                sum += 1
                carry = False
            if sum >= 10:
                sum -= 10
                carry = True
            sumNode = ListNode(sum)
            stack.append(sumNode)
            l1 = l1.next
            l2 = l2.next
        #If one is longer than the other
        while(l1):
            sum = l1.val + 1 if carry else l1.val
            if sum >= 10:
                sum -= 10
                carry = True
            else:
                carry = False
            newNode = ListNode(sum)
            stack.append(newNode)
            l1 = l1.next
        while(l2):
            sum = l2.val + 1 if carry else l2.val
            if sum >= 10:
                sum -= 10
                carry = True
            else:
                carry = False
            newNode = ListNode(sum)
            stack.append(newNode)
            l2 = l2.next
        if carry: #Create a new node if there is carry at the end
            newNode = ListNode(1)
            stack.append(newNode)
        prevNode = None
        headNode = None
        while(len(stack) > 0): #Generate resulting linked list
            headNode = stack.pop()
            headNode.next = prevNode
            prevNode = headNode
        return headNode



