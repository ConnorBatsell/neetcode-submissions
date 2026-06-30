class CountSquares:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
        self.cnt[tuple(point)]+=1
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        q = []
        res = 0
        for px,py in self.pts:
            if abs(point[0]-px)==abs(point[1]-py) and not point[0]==px:
                if self.cnt.get((point[0],py)) and self.cnt.get((px,point[1])):
                    res += self.cnt[(point[0],py)]*self.cnt[(px,point[1])]
        return res
        
            