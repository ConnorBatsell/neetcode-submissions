class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []
        self.following[userId].add(userId)
        for user in self.following[userId]:
            if user in self.tweets:
                index = len(self.tweets[user])-1
                time, tweetId = self.tweets[user][index]
                heapq.heappush(heap, [time, tweetId, user, index-1])
        while heap and len(res)<10:
            time, tweetId, user, index = heapq.heappop(heap)
            res.append(tweetId)
            if index>=0:
                count, tweetId = self.tweets[user][index]
                heapq.heappush(heap, [count, tweetId, user, index-1])
        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
