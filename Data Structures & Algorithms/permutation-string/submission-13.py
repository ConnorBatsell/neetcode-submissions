class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False
        want = Counter(s1)
        window = Counter(s2[:n])
        if want==window:
            return True
        for r in range(n, len(s2)):
            window[s2[r]]+=1
            window[s2[r-n]]-=1
            if want == window:
                return True
        return False


