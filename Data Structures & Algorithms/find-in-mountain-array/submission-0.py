class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l,r = 0, mountainArr.length()-1
        while l<=r:
            m = l + ((r-l)//2)
            if mountainArr.get(m) < mountainArr.get(m+1):
                l = m+1
            else:
                r=m-1
        lTwo = 0
        rTwo = l
        while lTwo <= rTwo:
            m = (lTwo + rTwo)//2
            if mountainArr.get(m) == target:
                return m
            elif mountainArr.get(m) < target:
                lTwo = m+1
            else:
                rTwo = m-1
        lThree = l
        rThree = mountainArr.length()-1
        while lThree <= rThree:
            m = (lThree + rThree)//2
            if mountainArr.get(m)==target:
                return m
            elif mountainArr.get(m) > target:
                lThree = m+1
            else:
                rThree = m-1
        return -1
            
            
