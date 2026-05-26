class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for n in asteroids:
            while s and n<0 and s[-1]>0:
                diff = s[-1] + n
                if diff>0:
                    n=0
                elif diff <0:
                    s.pop()
                else:
                    n=0
                    s.pop()
            if n:
                s.append(n)
        return s



        