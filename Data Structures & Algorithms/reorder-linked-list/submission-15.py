# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        curr = head
        n = []
        while curr:
            n.append(curr)
            curr = curr.next
        l,r = 0, len(n)-1
        while l<r:
            n[l].next = n[r]
            l+=1
            if l>=r:
                break
            n[r].next = n[l]
            r-=1
        n[l].next = None

        

        
