class MyCircularQueue:
    """
    1 Aug 2026
    - queue: FIFO
    - last position connected to first position -> circle
    benefits
    - space efficiency
        - normal queue: pop front element but the space infront not used
            - uses doubly linked list and not array cause array pop from front is O(n)
        - circular queue: pop front element, back still can append new elements in front
    - implement
        - initialise with size k
        - get front item. if empty return -1
        - get rear item
        - enqueue. return true if successful
        - dequeue
        - check if is empty
        - check if is full

    no using built in queue DS

    doubts:
    - enqueue but no space?

    idea
    - linked list vs array
        - all O(1) time complexity
        - you could use LL but the idea of question is to init a FIXED size array k and to reuse empty front slots
            LL same space but has pointer overheads

    array
    - init
        - array
        - front index as 0
        - count of elements (can determine the rear index by front + count % k)
    - enqueue
        adds at the rear ( rear + 1 )
        if rear + 1 == front -> No more space
        - if >= k reached the end, reset rear_index % k
    - dequeue
        remove from front (front + 1)
        - if >= k reached the end, reset front_index if can

    - full if [rear_index, front_index, ....]
    - empty if [front_index == rear_index, ....]

    index: modulo by the size of the list top get correct index

    mistake: it is not easy to track full/empty just with the front/read pointer. a 
    """

    def __init__(self, k: int):
        self.k = k
        self.queue = [0] * k
        self.front_index = 0
        self.count = 0
        
    def enQueue(self, value: int) -> bool:
        """
        if full, don't enqueue -> return False
        else add to the rear
            - add to the queue
            - increment count

        * rear index = index at the back TO insert new element, not the index of current last element. Contradicting to front_index which is the index of the front most element. Got extra + 1. Eg [4, 2], front_index = 0 and the count is 2, rear index is 2 (1-indexed)
        
        don't need to update values cleanly and clear if you know the start and end
        """
        if self.isFull():
            return False
        # add to queue: Increment count
        rear_index_to_insert = (self.front_index + self.count) % self.k
        self.queue[rear_index_to_insert] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        # If empty, nothing to deque -> return False
        if self.isEmpty():
            return False
        
        # Else, remove from queue. Decrement count + increment front
        self.front_index = (self.front_index + 1) % self.k
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front_index]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        rear_index = (self.front_index + self.count - 1) % self.k
        return self.queue[rear_index]
        

    def isEmpty(self) -> bool:
        return self.count == 0
        

    def isFull(self) -> bool:
        return self.count == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()