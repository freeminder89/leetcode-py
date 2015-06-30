__author__ = 'amow'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def connect(self, n1, n2):
        if not n1:
            return n2
        tn = n1.next
        n1.next = n2
        return self.connect(tn, n1)


    def reverseList(self, head):
        return self.connect(head, None)