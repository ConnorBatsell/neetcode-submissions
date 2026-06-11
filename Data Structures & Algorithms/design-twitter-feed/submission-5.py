class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)   # set avoids duplicate follows
        self.tweetIds = defaultdict(list)



    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetIds[userId].append((self.time, tweetId))
        self.time+=1


    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        for user in self.following[userId] | {userId}:
            for t, tweet in self.tweetIds[user]:
                out.append((t, tweet))
        out.sort(reverse=True)
        return [tweet for t, tweet in out[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
