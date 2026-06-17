class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = defaultdict(int)
        for bill in bills:
            change = bill-5
            count[bill]+=1
            if change==5: 
                if count[change]>0:
                    count[change]-=1
                else:
                    return False
            elif change==15:
                if count[5]>0 and count[10]>0:
                    count[5]-=1
                    count[10]-=1
                elif count[5]>2:
                    count[5]-=3
                else:
                    return False    
               


        return True