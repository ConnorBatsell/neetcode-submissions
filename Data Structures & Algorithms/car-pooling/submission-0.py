class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        newList = sorted(trips, key=lambda x: x[1])
        passengers = 0
        print(newList)
        for trip in newList:
            
            while heap and heap[0][0]<=trip[1]:
                a,b = heapq.heappop(heap)
                passengers = passengers - b
            if passengers+trip[0]>capacity:
                return False
            else:
                heapq.heappush(heap, [trip[2], trip[0]])
                passengers += trip[0]
        return True

