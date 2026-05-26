class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        s = []
        for i in range(len(temperatures)):
            result.append(0)
            for j in range(i, len(temperatures)):
                if(temperatures[j]>temperatures[i]):
                    result[i] = j-i
                    break
            
        return result
                
                
        
        