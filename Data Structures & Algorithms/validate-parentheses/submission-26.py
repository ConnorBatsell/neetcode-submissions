class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(', '}':'{', ']':'['}
        for c in s:
            print(c)
            if c=='(' or c=='[' or c=='{':
                stack.append(c)
            else:
                
                if stack and stack[-1]==dic[c]:
                    stack.pop()
                else:
                    return False
        return stack==[]

            