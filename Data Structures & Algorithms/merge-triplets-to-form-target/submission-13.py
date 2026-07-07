class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for i in range(len(triplets)):
            a = triplets[i]
            if a[0]>target[0] or a[1]>target[1] or a[2]>target[2]:
                continue
            for j in range(len(a)):
                if a[j]==target[j]:
                    good.add(j)
        return len(good)==3