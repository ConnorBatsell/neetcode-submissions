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
        group_prev = dummy

        while True:
            kt = group_prev
            for _ in range(k):
                kt = kt.next
                if not kt:
                    return dummy.next
            group_next = kt.next
            prev,curr = group_next, group_prev.next
            while curr!=group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            tmp = group_prev.next
            group_prev.next = kt
            group_prev = tmp

