class MyStack:
    """
    Stack: O(1) peek/pop from back. Append to the back

    Queue: pop from the front

    idea reverse the queue such that top is at the front
    - push:
        - add element to empty queue
        - add other elements to the back of it
    """
    from collections import deque

    def __init__(self):
        self.main_queue = deque()
        self.empty_queue = deque()
        
    def push(self, x: int) -> None:
        self.empty_queue.append(x) # add to empty queue

        # populate empty queue with x in the front
        while self.main_queue:
            self.empty_queue.append(self.main_queue.popleft())
        
        # swap back at the end
        self.empty_queue, self.main_queue = self.main_queue, self.empty_queue
        
    def pop(self) -> int:
        return self.main_queue.popleft()

    def top(self) -> int:
        return self.main_queue[0]

    def empty(self) -> bool:
        print(self.main_queue)
        return not self.main_queue
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()