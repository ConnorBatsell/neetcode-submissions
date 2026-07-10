class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dA = defaultdict(int)
        dB = defaultdict(int)
        for i in range(len(s)):
            dA[s[i]]+=1
            dB[t[i]]+=1
        return dA==dB