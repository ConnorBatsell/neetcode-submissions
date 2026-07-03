class Twitter:

    def __init__(self):
        self.t = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.t, tweetId])
        self.t+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        self.following[userId].add(userId)
        for user in self.following[userId]:
            if user in self.tweets:
                idx = len(self.tweets[user])-1
                time,tweetId = self.tweets[user][idx]
                heapq.heappush(heap, [-time, tweetId, idx, user])
        while heap and len(res)<10:
            time,tweetId,idx,user = heapq.heappop(heap)
            res.append(tweetId)
            if idx>0:
                t,tw = self.tweets[user][idx-1]
                heapq.heappush(heap, [-t,tw,idx-1,user])
        return res
            



    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)