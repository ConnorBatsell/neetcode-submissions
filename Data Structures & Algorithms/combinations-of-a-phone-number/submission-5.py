class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if not digits:
            return []
        res = []
        sub = []
        def dfs(i):
            if i>=len(digits):
                res.append("".join(sub))
                return
            chars = mapping[digits[i]]
            for c in chars:
                sub.append(c)
                dfs(i+1)
                sub.pop()
        dfs(0)
        return res

            
                    
