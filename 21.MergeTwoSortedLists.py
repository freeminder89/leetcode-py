__author__ = 'amow'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        head = tail = None
        while True:
            if l1.val > l2.val:
                if tail:
                    tail.next = l2
                    tail = tail.next
                else:
                    tail = l2
                l2 = l2.next
            else:
                if tail:
                    tail.next = l1
                    tail = tail.next
                else:
                    tail = l1
                l1 = l1.next
            if not head:
                head = tail
            if not l1:
                tail.next = l2
                return head
            elif not l2:
                tail.next = l1
                return head