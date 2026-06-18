class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexC = defaultdict(int)
        for i,c in enumerate(s):
            indexC[c] = i
        out = []
        end = 0
        size = 0 #okay skinny!!!
        for i,c in enumerate(s):
            end = max(end,indexC[c]) 
            size+=1
            if i==end: #WEWEORJWEORJWOEJROIWEJROIWJEROIJWEORJOWEIR PENIS PENIS PENIS
                out.append(size)
                end = 0
                size = 0
                
        return out
