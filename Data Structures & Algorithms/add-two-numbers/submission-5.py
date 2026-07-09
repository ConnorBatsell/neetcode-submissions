# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier = 1
        p = 0
        curr = l1
        while curr:
            p += multiplier*curr.val
            multiplier*=10
            curr = curr.next
        multiplier = 1
        pTwo = 0
        curr = l2
        while curr:
            pTwo += multiplier*curr.val
            multiplier*=10
            curr = curr.next
        res = str(p+pTwo)
        head = ListNode(0)
        curr = head
        for c in res[::-1]:
            curr.next = ListNode(int(c))
            curr = curr.next
        return head.next
        