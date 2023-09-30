class Twitter:

    def __init__(self):
        self.postT = 0
        self.followsMap = defaultdict(set)
        self.tweetsMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsMap[userId].append([self.postT, tweetId])
        self.postT -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minTweetHeap = []
        
        self.followsMap[userId].add(userId)
        #print(self.followsMap[userId])
        for followeeId in self.followsMap[userId]:
            if followeeId in self.tweetsMap: #self.tweetMap.keys()
                index = len(self.tweetsMap[followeeId]) - 1
                cnt, tweetId = self.tweetsMap[followeeId][index]
                minTweetHeap.append([cnt, tweetId, followeeId, index - 1])
            heapq.heapify(minTweetHeap)
        while minTweetHeap and len(res) < 10:
            cnt, tweetId, followeeId, index = heapq.heappop(minTweetHeap)
            res.append(tweetId)
            if index >= 0:
                cnt, tweetId = self.tweetsMap[followeeId][index]
                heapq.heappush(minTweetHeap, [cnt, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followsMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followsMap[followerId]:
            self.followsMap[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)