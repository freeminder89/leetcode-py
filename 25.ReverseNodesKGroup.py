# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverse_k(self, start, k):
        i = start
        cnt = 0
        while i is not None and cnt < k:
            i = i.next
            cnt += 1
        if cnt != k:
            return None, None
        current = start
        head = current
        tail = head
        while cnt > 0:
            if current == start:
                cnt -= 1
                current = current.next
                continue
            reserve = current.next
            current.next = head
            head = current
            current = reserve
            cnt -= 1
            if cnt == 0:
                tail.next = current
        return head, tail

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        pre = None
        result = head
        while True:
            start = head if pre is None else pre.next
            rhead, rtail = self.reverse_k(start, k)
            if rhead is None:
                break
            if pre is not None:
                pre.next = rhead
            else:
                result = rhead
            pre = rtail
        return result


class Node():
    def __init__(self, v):
        self.v = v
        self.next = None

    def __str__(self):
        return self.v


def build_from_list(li):
    head = Node(li[0])
    pre = head
    for i in range(1, len(li)):
        n = Node(li[i])
        pre.next = n
        pre = n
    return head


def print_node(head):
    s = head
    li = []
    while s is not None:
        li.append(s.v)
        s = s.next
    print li


fun = lambda x, y: print_node(Solution().reverseKGroup(build_from_list(range(x)), y))

fun(10, 10)
