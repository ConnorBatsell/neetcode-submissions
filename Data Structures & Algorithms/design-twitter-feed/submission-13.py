class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        self.following[userId].add(userId)
        for user in self.following[userId]:
            if user in self.tweets:
                indx = len(self.tweets[user])-1
                time, tweetId = self.tweets[user][indx]
                heapq.heappush(heap, [-time, tweetId, user, indx])
        while heap and len(res)<10:
            time, tweetId, user, indx = heapq.heappop(heap)
            res.append(tweetId)
            if indx>0:
                ti, twe = self.tweets[user][indx-1]
                heapq.heappush(heap, [-ti, twe, user, indx-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)        
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
