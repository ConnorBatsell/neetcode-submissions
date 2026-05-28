class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair =[]
        for i in range(len(position)):
            pair.append([position[i], speed[i]])
        sta=[]
        for p,s in sorted(pair)[::-1]:
            time = (target-p)/s
            sta.append(time)
            if len(sta)>=2 and sta[-1] <=sta[-2]:
                sta.pop()
        return len(sta)
                