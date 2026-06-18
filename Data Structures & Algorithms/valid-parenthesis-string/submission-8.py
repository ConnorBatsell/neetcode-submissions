class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        count = 0
        for i in range(len(s)):
            c = s[i]
            if c==')':
                if stack:
                    stack.pop()
                else:
                    if star:
                        star.pop()
                    else:
                        return False
            elif c=='*':
                star.append(i)
            else:
                stack.append(i)
        while stack and star:
            if stack.pop() > star.pop():
                return False
        return not stack
