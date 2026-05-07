class User:
    def __init__(self, userId):
        self.userId = userId
        self.followings = set()

    def follow(self, followeeId):
        self.followings.add(followeeId)
    
    def unfollow(self, followeeId):
        if followeeId in self.followings:
            self.followings.remove(followeeId)

    def getFollowings(self):
        return self.followings

    # user has tweets identified by userId
    # user has a list of people they follow, pointing to their user instances

class Twitter:

    def __init__(self):
        self.array = [] # stores sequential tweets, least to most recent
        self.users = {} # maps userIds to their objects

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.array.append((userId, tweetId))
        if userId not in self.users:
            user = User(userId)
            self.users[userId] = user
        # user = self.users[userId]
        # user.follow(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        # gets 10 most recent tweet IDs across all users including userId himself
        user = self.users[userId]
        followings = user.getFollowings()
        newsFeed = []
        counter = 0
        for user, tweet in reversed(self.array):
            if user not in followings and user != userId:
                continue
            newsFeed.append(tweet)
            counter += 1
            if counter == 10:
                break
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        user = self.users[followerId]
        user.follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user = self.users[followerId]
        user.unfollow(followeeId)
        
