class FreqStack:

    def __init__(self):
        self.m = {}
        self.stack = {}
        self.maxs = 0

    def push(self, val: int) -> None:
        count = 1
        if val in self.m:
            count = self.m[val] +1
        self.m[val] = count
        if count > self.maxs:
            self.maxs = count
            self.stack[count] = []
        self.stack[count].append(val)
        
    def pop(self) -> int:
        res = self.stack[self.maxs].pop() 
        self.m[res] -= 1
        if not self.stack[self.maxs]:
            self.maxs -=1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()