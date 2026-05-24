class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for n in operations:
            if n=='D':
                record.append(record[-1]*2)
            elif n=='C':
                record.pop()
            elif n=='+':
                record.append(sum(record[-2:]))
            else:
                record.append(int(n))
        return sum(record)
