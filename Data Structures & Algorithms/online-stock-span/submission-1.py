class StockSpanner:
    """
    26 Aug 2026
    question
    - insert price and return span
    - span is the no of consecutive days before (including today)
        where price < today
    
    bruteforce
    - every next
        - go through every element to check if today greater than each prev price O(n)
    
    optimal idea - monotonic decreasing (maintain decreasing)
    - if meet an increasing today high price, pop from stack until today is lower price
    - need a way to optimally get the span without searching every previous element
    - stack stores (price, span)
        - after popping, the span is reflects and you will sum the spans
    
    <=
    Time: Ammortised O(1) per operation because not every next() call goes through whole stack. Total sum is O(n)
    Space: O(n) stack
    17:23
    """

    def __init__(self):
        self.stack = [] # monotonic decreasing (price, span)

    def next(self, price: int) -> int:
        cur_span = 1 # include itself
        while self.stack and self.stack[-1][0] <= price: # while today price is more/equal than previous days
            prev_price, prev_span = self.stack.pop()
            cur_span += prev_span
        self.stack.append((price, cur_span))
        return cur_span


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)