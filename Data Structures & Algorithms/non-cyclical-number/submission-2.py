class Solution:
    def isHappy(self, n: int) -> bool:
        q = deque()
        s = 0 
        while n:
            dig = n%10
            s += dig**2
            n = n//10
        if not s==1:
            while not s in q:
                q.append(s)
                prev = s
                s = 0
                while prev:
                    dig = prev%10
                    s += dig**2
                    prev = prev//10
                if s==1:
                    return True
            return False

        return True