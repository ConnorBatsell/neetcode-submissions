# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for lst in lists:
            while(lst):
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        dummy = ListNode(0)
        current = dummy
        for node in nodes:
            current.next = ListNode(node)
            current = current.next
        return dummy.next

            

        

        