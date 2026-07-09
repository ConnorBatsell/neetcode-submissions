class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev,nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        end = self.right.prev
        end.next = node
        node.prev = end
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.dic:
            self.remove(self.dic[key])
            self.insert(self.dic[key])
            return self.dic[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.remove(self.dic[key])
        self.dic[key] = Node(key, value)
        self.insert(self.dic[key])

        if len(self.dic)>self.cap:
            temp = self.left.next
            self.remove(temp)
            del self.dic[temp.key]
            