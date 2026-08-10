class Twitter:

    """
    Idea:
    - get the top k -> heap
    - collect all his following's tweets

    rejected) Each user pre stores their feed
        - every post call -> update follower's feed
        - user has list of followers, and following
            - and does not have a store for post
            - but rather a store for feed
        -> have to see write or read is more often
        * but problem is, when unfollow - how to remove from feed
    
    look below) getNewsFeed is only retrieved on call
        - only then you just need a following list and search.
        - user just need a following list and their own posts

    - either way you need a heap for the feed to get the msot recent
        - CANNOT assume tweetId is incremental and in order 







    2) method
    - user: userId: SET of following userIds (set is O(1) lookup compared to list)
    - posts: userId: tweetIds
    for both - use hashmap for easy access

    - tweetId may not be in numerically ordered -> need a tuple count to keep track of time
    - novel idea:
        - similar to merge k sorted list -> use a min heap to find the min
        at every step between multiple lists
    """

    from collections import defaultdict
    import heapq
    def __init__(self):
        """
        follow_map
        - userId: set of following userIds

        posts_map
        - userId: list of posts (time, tweetId)
            - not a set because you want to maintain the order of insertion (sorted)
                - this way you can do merge k sorted

        """
        self.follow_map = defaultdict(set) # return a default set when calling missing key
        self.posts_map = defaultdict(list)
        self.time = 0 # since python default is min heap and we finding the most recent -> increment negatively

    def postTweet(self, userId: int, tweetId: int) -> None:
        # tweetId is unique
        self.time -= 1
        self.posts_map[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # returns ordered 10 most recent tweetIds -> posted by userId himself of those he follow
        min_heap = []

        # Initialising
        self.follow_map[userId].add(userId) # For case where user's own post is counted
        for followee_id in self.follow_map[userId]: # For each user cur userId is following
            if followee_id in self.posts_map: # followee may not have any posts
                followee_posts = self.posts_map[followee_id]
                i = len(followee_posts) - 1

                # want most recent -> get from back in reverse.
                # Also include followee_id for later retrieval -> to get next ele
                latest_time, latest_tweetId = followee_posts[i]
                min_heap.append((latest_time, latest_tweetId, followee_id, i))     
        heapq.heapify(min_heap) # O(n)

        k = 1
        result = []
        # min_heap will be empty when there are no more elements left
        while k <= 10 and min_heap:
            latest_time, latest_tweetId, followee_id, i = heapq.heappop(min_heap)
            result.append(latest_tweetId)

            # Add next i - 1 post in the followee_id's posts list
            if i - 1 >= 0:
                nxt_time, nxt_tweetId = self.posts_map[followee_id][i - 1]
                heapq.heappush(min_heap, (nxt_time, nxt_tweetId, followee_id, i - 1))
            k += 1

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]: # may not even be following in the first place
            self.follow_map[followerId].remove(followeeId)
        # or use .discard
        
