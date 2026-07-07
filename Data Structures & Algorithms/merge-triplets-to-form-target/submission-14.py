class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x=y=z=False
        for a in triplets:
            x |= target[0]==a[0] and a[1]<=target[1] and a[2]<=target[2]
            y |= a[0]<=target[0] and a[1]==target[1] and a[2]<=target[2]
            z |= a[0]<=target[0] and a[1]<=target[1] and a[2]==target[2]
        return x and y and z