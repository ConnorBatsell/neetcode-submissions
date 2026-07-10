# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        start = dummy
        while True:
            kth = start
            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            nxtGroup = kth.next
            prev = nxtGroup
            curr = start.next
            while curr!=nxtGroup:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = start.next
            start.next = kth
            start = tmp


            


