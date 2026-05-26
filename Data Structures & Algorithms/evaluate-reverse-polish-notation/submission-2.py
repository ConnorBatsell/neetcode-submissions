class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for c in tokens:
            if c=="+":
                s.append(int(s.pop()) + int(s.pop()))
            elif c=="-":
                a = int(s.pop())
                b = int(s.pop())
                s.append(b-a)
            elif c=="*":
                s.append(int(s.pop()) * int(s.pop()))
            elif c=="/":
                a = int(s.pop())
                b = int(s.pop())
                s.append(b/a)
            else:
                s.append(c)
        if(s):
            return int(s[0])
        return None
        