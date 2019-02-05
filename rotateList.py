# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getLength(self, head: 'ListNode'):
        length = 0
        curr = head
        while curr: # Count number of elements in list
            length += 1
            curr = curr.next
            
        return length
        
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        length = self.getLength(head)
        if length <= 1 or k % length == 0:
            return head
                    
        remain = length - (k % length) - 1 # If k > length
        
        curr = head
        while remain: # Traverse to rotate pos
            remain -= 1
            curr = curr.next
            
        newHead = curr.next # Save new head and cut old list
        curr.next = None
        
        curr = newHead
        while curr.next: # Traverse to the end and append previous list
            curr = curr.next
            
        curr.next = head
        return newHead
