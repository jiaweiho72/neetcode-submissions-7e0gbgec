class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        23 Aug 2026
        each boat
        - boat carries <= 2 people
        - boat must be within weight limit

        return min no of boats to carry everyone

        Question
        - group 1-2 nums where sum <= limit
        - return min no of groups

        idea
        - greedily put the largest and smallest together
            - greedy always optimal
            - if x + y = limit
                - there is nothing more optimal if y was swapped with a smaller number
            - if you saved y for another pair, yes still can form a pair but it may not be optimal, as now there may not be a perfect for x and x remains by itself. 

        - sort and two pointer
        smallest -> largest
        eg. limit = 10
        [1,2,3,6]
        pair smallest 1 to largest 6 works
        
        I thought that is there a case where smallest+largest is very far from the limit and I can choose a larger small value. 
        - then in the mid, two large mids sum exceeds limit as a result
        - what if we left the smallest for the mid to use
        eg. limit = 25
        [1,7,12,13]
        if greedy, 1+7, 3+6, X5+6
        what if I used
        if 3+7, 

        no such case. 
        for the second smallest: 7 + 13 = 20 <= 25
        this also means that the sum of 7 and any middle number like 12 is always <20
        - basically: when finding small complement for the largest number
            - even if you chose smallest number 1 and leave as option the largest small number 7
                - the sum of 7 and any mid number will ALWAYS be smaller than that of the sum of 7 and the largest and thus valid. 
                - thus, to solve a mid1 + mid2 that is too high,  you can use any of the valid numbers that can sum with the largest number. Everyone of it works
                    - because if it can sum with the largest, it can sum with anything smaller than the largest which is everything
        - conclusion: there is no need to find the largest smallest number


        - need to fit the largest with the largest smallest
        """

        people.sort()
        n = len(people)
        l, r = 0, n - 1
        no_of_boats = 0
        while l <= r: # equals so that
            pair_sum = people[l] + people[r]
            if pair_sum > limit: # exceeded - single boat
                r -= 1
            else: # pair formed
                l += 1
                r -= 1

            no_of_boats += 1

        return no_of_boats






