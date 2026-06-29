class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        multiplier = 1
        out = 1
        while len(digits)>0:
            out += digits.pop()*multiplier
            multiplier*=10
        res = []
        while out>0:
            res.append(out%10)
            out = out//10
        return res[::-1]