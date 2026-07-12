class MinStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        self.s1.append(val)
        if self.s2 and val<self.s2[-1]:
            self.s2.append(val)
        elif self.s2:
            self.s2.append(self.s2[-1])
        else:
            self.s2.append(val)

    def pop(self) -> None:
        self.s1.pop()
        self.s2.pop()
        
    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]
        
        
