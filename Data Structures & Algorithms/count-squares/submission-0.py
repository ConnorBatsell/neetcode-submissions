class CountSquares:

    def __init__(self):
        self.cnt = Counter()

    def add(self, point: List[int]) -> None:
        self.cnt[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        q = []
        res = 0
        for (px,py),c in self.cnt.items():
            if abs(point[0]-px)==abs(point[1]-py) and not point[0]==px:
                res += c*self.cnt[(point[0],py)]*self.cnt[(px,point[1])]
        return res
        
            