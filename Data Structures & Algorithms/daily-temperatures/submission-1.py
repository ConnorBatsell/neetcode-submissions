class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        s = []
        for i,j in enumerate(temperatures):
            while s and j>s[-1][0]:
                stackTemp, stackIndex = s.pop()
                result[stackIndex] = i-stackIndex
            s.append([j,i])
            
            
        return result
                
                
        
        