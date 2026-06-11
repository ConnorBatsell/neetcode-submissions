class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)   # set avoids duplicate follows
        self.tweetIds = defaultdict(list)



    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetIds[userId].append((self.time, tweetId))
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for user in self.following[userId] | {userId}:
            tweets = self.tweetIds[user]
            if tweets:
                idx = len(tweets) - 1                    # most recent
                ts, tweetId = tweets[idx]
                heapq.heappush(heap, (-ts, tweetId, user, idx))   # -ts → max-heap

        res = []
        while heap and len(res) < 10:
            neg_ts, tweetId, user, idx = heapq.heappop(heap)
            res.append(tweetId)
            if idx > 0:                                  # older tweet from same user?
                idx -= 1
                ts, older = self.tweetIds[user][idx]
                heapq.heappush(heap, (-ts, older, user, idx))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
