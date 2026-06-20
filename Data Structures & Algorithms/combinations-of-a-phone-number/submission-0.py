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
        a=[]
        if not digits:
            return []
        def dfs(i, path):
            if i==len(digits):
                res.append("".join(path.copy()))
                return
            for j in range(len(digitToChar[digits[i]])):
                c = digitToChar[digits[i]][j]
                path.append(c)
                dfs(i+1, path)
                path.pop()
        dfs(0,a)
        return res

            
                    
