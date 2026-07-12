class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        for i,t in enumerate(temperatures):
            while s and s[-1][0]<t:
                a,b = s.pop()
                res[b] = i-b
            s.append([t,i])
        return res
                
        
        