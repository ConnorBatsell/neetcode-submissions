class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            curr = ''.join(sorted(s))
            d[curr].append(s)
        res = []
        for key,val in d.items():
            res.append(val)
        return res