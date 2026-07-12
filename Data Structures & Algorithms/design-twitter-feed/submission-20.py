class Twitter:

    def __init__(self):
        self.t = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.t+=1
        self.tweets[userId].append([tweetId, self.t])       

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        self.following[userId].add(userId)
        h = []
        for user in self.following[userId]:
            if self.tweets[user]:
                idx = len(self.tweets[user])-1
                tweetId, time = self.tweets[user][idx]
                heapq.heappush(h, (-time, tweetId, idx, user))
        while h and len(res)<10:
            time, tweetId, idx, user = heapq.heappop(h)
            res.append(tweetId)
            if idx>0:
                tweetId, time = self.tweets[user][idx-1]
                heapq.heappush(h, (-time, tweetId, idx-1, user))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)

