"""
We need to track two things
- tweet ctr, tweet ID
- everyone the user is following

we're tracking from the follower's perspective. Easier to form the newsfeed
"""


class Twitter:

    def __init__(self):
        self.following_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.tweet_ctr = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.tweet_ctr, tweetId))

        if len(self.tweet_map[userId]) > 10:
            self.tweet_map[userId].pop(0)

        self.tweet_ctr += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        profiles_followed = self.following_map[userId] | set([userId])

        tweet_heap = []
        res = []

        for user_profile in profiles_followed:
            for tweet in self.tweet_map[user_profile]:
                heapq.heappush_max(tweet_heap, tweet)
            
        while tweet_heap and len(res) < 10:
            res.append(heapq.heappop_max(tweet_heap)[1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_map[followerId]:
            self.following_map[followerId].remove(followeeId)
        
