class Solution:
    def isValid(self, s: str) -> bool:
        sta = []
        matches = {")": "(", "]" : "[", "}" : "{"}
        for c in s:
            if c in matches:
                if sta and sta[-1]==matches[c]:
                    sta.pop()
                else:
                    return False;
            else:
                sta.append(c)
        return True if not sta else False
            