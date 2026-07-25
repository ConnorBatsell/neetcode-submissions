class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        if not digits:
            return []
        sub = []
        def dfs(i):
            if i>=len(digits):
                res.append("".join(sub.copy()))
                return
            temp = digitToChar[digits[i]]
            for j in range(len(temp)):
                sub.append(temp[j])
                dfs(i+1)
                sub.pop()
        dfs(0)
        return res

            
                    
