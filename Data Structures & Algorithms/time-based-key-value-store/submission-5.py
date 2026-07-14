class TimeMap:

    def __init__(self):
        self.t = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.t:
            self.t[timestamp] = {}
            self.t[timestamp][key] = value
        else:
            self.t[timestamp][key] = value

    def get(self, key: str, timestamp: int) -> str:
        for i in range(timestamp, -1, -1):
            if i in self.t:
                if key in self.t[i]:
                    return self.t[i][key]
        return ""

        
