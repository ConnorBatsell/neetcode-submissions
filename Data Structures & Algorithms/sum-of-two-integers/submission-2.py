class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        res = 0
        for i in range(0,32):
            c = (a>>i)&1
            d = (b>>i)&1
            out = c ^ d ^ carry
            res |= out << i
            if c + d + carry>=2:
                carry=1
            else:
                carry = 0
            
        if res >= (1 << 31):     # bit 31 set → negative in two's complement
            res -= (1 << 32)
        return res
