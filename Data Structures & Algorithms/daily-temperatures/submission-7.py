class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        for i,t in enumerate(temperatures):
            while s and s[-1][0] < t:
                temp,indx = s.pop()
                res[indx] = i-indx
            s.append([t,i])
        return res
                
        
        