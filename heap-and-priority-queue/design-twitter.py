"""Design Twitter
Design a simplified version of Twitter where users can post tweets, 
follow/unfollow another user, 
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

- Twitter() 
    Initializes your twitter object.
- void postTweet(int userId, int tweetId) 
    Composes a new tweet with ID tweetId by the user userId. 
    Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) 
    Retrieves the 10 most recent tweet IDs in the user's news feed. 
    Each item in the news feed must be posted by users 
    who the user followed or by the user themself. 
    Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) 
    The user with ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) 
    The user with ID followerId 
    started unfollowing the user with ID followeeId.
"""

import collections
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.totalTweetCount = 0
        # user id: [(time, tweet ids)]
        self.tweets = collections.defaultdict(list)
        # users id : [following user ids]
        self.followings = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.totalTweetCount += 1
        self.tweets[userId].append((self.totalTweetCount, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        self.followings[userId].add(userId)
        for following in self.followings[userId]:
            for time, tweet in self.tweets[following]:
                newsFeed.append((-time, tweet))
        heapq.heapify(newsFeed)

        orderedNewsFeed = []
        for _ in range(10):
            if not newsFeed:
                break
            time, tweet = heapq.heappop(newsFeed)
            orderedNewsFeed.append(tweet)
        return orderedNewsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if (followerId == followeeId 
            or followeeId in self.followings[followerId]):
            return
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (followerId == followeeId 
            or followeeId not in self.followings[followerId]):
            return
        self.followings[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)