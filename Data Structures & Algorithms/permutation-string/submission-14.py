class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = len(s1)
        if a > len(s2):
            return False
        need = Counter(s1)
        window = Counter(s2[:a])
        if need == window:
            return True
        for r in range(a, len(s2)):
            window[s2[r-a]]-=1
            window[s2[r]]+=1
            if window==need:
                return True
        return False



