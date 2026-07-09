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
            # walk k nodes ahead to find the group's last node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:          # fewer than k left → leave as-is, done
                    return dummy.next
            group_next = kth.next     # first node of the NEXT group (stash before mutating)

            # reverse [group_prev.next .. kth], pointing everything toward group_next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # reconnect: old first node becomes the tail and the new group_prev
            tmp = group_prev.next
            group_prev.next = kth     # attach new head of reversed group
            group_prev = tmp
