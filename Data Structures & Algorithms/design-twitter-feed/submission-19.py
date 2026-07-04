class Twitter:

    def __init__(self):
        self.t = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.t, tweetId])
        self.t += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        self.following[userId].add(userId)
        for user in self.following[userId]:
            if len(self.tweets[user])>0:
                idx = len(self.tweets[user])-1
                time,tweetId = self.tweets[user][idx]
                heapq.heappush(h, [-time, tweetId, user, idx])
        out = []
        while h and len(out)<10:
            t,tw,u,ix = heapq.heappop(h)
            out.append(tw)
            if ix>0:
                time,tweetId = self.tweets[u][ix-1]
                heapq.heappush(h, [-time,tweetId,u,ix-1])
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)