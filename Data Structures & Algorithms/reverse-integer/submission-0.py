class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        rev = s[::-1]
        if rev[-1]=="-":
            rev = "-"+rev[:len(rev)-1]
        n = int(rev)
        if not (-2**31) <= n <= ((2**31)-1):
            return 0
        return n