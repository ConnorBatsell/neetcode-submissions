"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = {}
        cur = head
        while cur:
            temp[cur] = Node(cur.val)
            cur = cur.next
        temp[None] = None
        curr = head
        while curr:
            temp[curr].next = temp[curr.next]
            temp[curr].random = temp[curr.random]
            curr = curr.next
        return temp[head]
        


    