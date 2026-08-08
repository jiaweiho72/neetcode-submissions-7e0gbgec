class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        8 Aug
        - return boolean if possible to create contiguous hands of groupSize

        Idea
        - the smallest element is always the bottleneck and you should process first
        - then try to form the hands starting from there. Decrement the card counts used
        - then move on to the next minimum 
        
        1) Gather a dict of counts of each cards
        2) As greedily start processing from the current smallest card, we have a min_heap to get the smallest everytime
            - min_heap values is all the unique card numbers
        while loop process min_card each time (one hand at a time)
            - build a hand of groupSize starting from min_card
                - for each number, check if there is enough count in the dict
                - if enough, use it
                    - decrement count
                - if count reach 0
                    - if it's the starting min_num it is ok, then just pop this from min_heap and start from the next smallest
                    - else, if in between not enough, means invalid. As the starting min_num had enough but could not form anything
        """
        from collections import Counter
        import heapq
        n = len(hand)
        # If not divisible
        if n % groupSize != 0:
            return False

        # 1) get counts
        card_count = dict(Counter(hand))
        # 2) Build min_heap
        min_heap = [key for key in card_count.keys()]
        heapq.heapify(min_heap)

        while min_heap:
            min_card = min_heap[0]
            for card in range(min_card, min_card + groupSize): # is must be able to form full -> else return False
                if card not in card_count: # not in available cards -> False
                    return False
                
                card_count[card] -= 1
                if card_count[card] == 0:
                    # use min_heap[0] as in this iteration you may need to move it multiple times and it won't just be once from min_card
                    if card == min_heap[0]: # if it is the first letter and is 0 -> just start from the next min number
                        heapq.heappop(min_heap) # remove current min_card
                    else: # min_num starting had enough but midway there is not enough to continue -> invalid
                        return False

                
                    
        # reach here means all finished and valid
        return True
            
            












        



