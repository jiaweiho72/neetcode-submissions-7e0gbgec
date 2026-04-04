class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        4 apr 2026

        notes
        - h time to complete bananas
        - decide bph k
        - you can't eat more than one pile per iteration

        return
        - MIN k to still complete all bananas within h hours

        - we are finding a min value of k where finish all piles in < h hours
            - bruteforce search trying all values of k 
                min = 0, max = max(piles)
            - speed up the search using BS
                - each time calculate time to complete forlooping through piles

        # 10mins
        """

        n = len(piles)
        # min is 1 to avoid 0 error and logically is not possible
        l, r = 1, max(piles) # range of possible values of speed k
        min_speed = float('inf')
        while l <= r:
            m = (l + r) // 2
            time_taken = 0
            for pile in piles:
                time_taken += math.ceil(pile / m)
            
            if time_taken <= h: # valid but you want try smaller value of speed
                min_speed = min(min_speed, m)
                r = m - 1
            else: # time_taken > h: overshot, need to increase speed to make faster
                l = m + 1

        return min_speed






