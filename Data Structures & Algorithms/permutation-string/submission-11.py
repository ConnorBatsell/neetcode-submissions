class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n>len(s2):
            return False
        need = Counter(s1)
        wind = Counter(s2[:n])
        if need == wind:
            return True
        for r in range(n, len(s2)):
            wind[s2[r]]+=1
            wind[s2[r-n]]-=1
            if wind[s2[r-n]]==0:
                del wind[s2[r-n]]
            if need==wind:
                return True
        return False


