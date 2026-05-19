"""
- We need to track followers and followees
- We only need to maintain 10 tweets from followers
- Each user should get their own heap limited to 10

If someone posts a tweet, all their followers' heaps get updated
If someone follows and unfollows then?

Should we maintain a heap with all tweets and then iterate through that?
If a user or their followees are in the heap, we go for it.

we'll have to pop and re-populate the heap -> Could be a max heap, so we could be good? Not necessarily

How about each user gets their own heap? Might be easier to iterate that and update that

But then when you unfollow, you'll have to filter it out, which is still fine. There's some overhead there
But let's say user unfollowed them because they tweet too much, we'll still be holding their tweets just in case the user follows them again.

What if we use a min heap and a max heap to track this?
Not seeing the worth here, we'll need to populate it, O(N) anyway

FINAL: EACH USER HAS THEIR OWN HEAP
We track who the user follows - For a user, we only track who the user follows
We do't care about their followers

On post, 
- We get all accounts that follow the poster
- we update their heap with the post

on getNewsFeed, for each user heap we check the user too, we limit to 10 and pop and re-populate

on follow, we add followerID to foloweeID's set because the follower gets the tweets
on unfollow we remove it


["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]
[null,null,null,[10],[20],null,[20,10],[20],null,[10]]
"""

class Twitter:

    def __init__(self):
        # Make this easy, track followers and followees
        # userID: set(Accounts user follows)
        self.follower_map = defaultdict(set)

        self.tweet_heap = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Add tweet to self tweets
        heapq.heappush_max(self.tweet_heap, (tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        temp_heap = []
        res = []
        temp = []

        # print(self.follower_map)
        # print(self.follower_map[userId] | set([userId]))
        print(self.tweet_heap)

        while self.tweet_heap:
            curr_tweet, curr_user = heapq.heappop_max(self.tweet_heap)

            if curr_user in (self.follower_map[userId] | set([userId])):
                heapq.heappush_max(res, curr_tweet)

            temp.append((curr_tweet, curr_user))        
    
        while temp:
            heapq.heappush_max(self.tweet_heap, temp.pop())

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        """
        self.follower_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_map[followerId].remove(followeeId)
        
